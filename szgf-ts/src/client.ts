import * as fs from 'fs/promises';
import * as path from 'path';
import { OriginalGuide } from './types';

/**
 * GitHub API content item representation.
 */
export interface GithubContentItem {
  /** The file or directory name */
  name: string;
  /** The type of content (file or directory) */
  type: string;
  /** The raw download URL for files */
  download_url?: string;
}

/**
 * Parsed guide with optional character ID.
 * Extends the base OriginalGuide with character ID support.
 */
export interface ParsedGuideWithId extends OriginalGuide {
  character: OriginalGuide['character'] & {
    /** Optional character ID for indexed access */
    id?: number;
  };
}

/**
 * SZGF Client for downloading and reading ZZZ character guides.
 *
 * @example
 * ```typescript
 * const client = new SZGFClient();
 *
 * // Download guides from GitHub
 * await client.downloadGuides();
 *
 * // Read guides from local storage
 * const guides = await client.readGuides();
 *
 * // Get a specific guide by character name
 * const ellenGuide = await client.getGuide('Ellen');
 * ```
 */
export class SZGFClient {
  private guidesUrl = 'https://api.github.com/repos/seriaati/zzz-guides/contents/guides/parsed';
  private guidesDir: string;

  /**
   * Creates a new SZGF client instance.
   * @param guidesDir - Directory to store downloaded guides (default: '.zzz_guides')
   */
  constructor(guidesDir: string = '.zzz_guides') {
    this.guidesDir = guidesDir;
  }

  /**
   * Fetch text content from a URL.
   */
  private async fetchText(url: string): Promise<string> {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.text();
  }

  /**
   * Fetch JSON data from a URL.
   */
  private async fetchJson<T>(url: string): Promise<T> {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json() as T;
  }

  /**
   * Download a single guide file.
   */
  private async downloadGuideFile(item: GithubContentItem): Promise<void> {
    if (!item.download_url) {
      throw new Error(`No download URL for ${item.name}`);
    }

    const content = await this.fetchText(item.download_url);
    const filePath = path.join(this.guidesDir, item.name);
    await fs.writeFile(filePath, content, 'utf-8');
  }

  /**
   * Download all guide files from the GitHub repository.
   * Creates a local directory (default: .zzz_guides) and downloads all JSON guide files.
   *
   * @throws {Error} If the download fails or network issues occur
   *
   * @example
   * ```typescript
   * await client.downloadGuides();
   * ```
   */
  async downloadGuides(): Promise<void> {
    console.log('Downloading guides...');

    const data = await this.fetchJson<GithubContentItem[]>(this.guidesUrl);

    // Create guides directory
    await fs.mkdir(this.guidesDir, { recursive: true });

    // Create .gitignore
    await fs.writeFile(
      path.join(this.guidesDir, '.gitignore'),
      '*\n',
      'utf-8'
    );

    // Download all JSON files in parallel
    const downloads = data
      .filter(item => item.type === 'file' && item.name.endsWith('.json'))
      .map(item => this.downloadGuideFile(item));

    await Promise.all(downloads);
    console.log(`✓ Downloaded ${downloads.length} guides`);
  }

  /**
   * Read all downloaded guides from local storage.
   *
   * @returns A dictionary mapping character IDs (or names) to their guide data
   * @throws {Error} If the guides directory doesn't exist (run downloadGuides first)
   *
   * @example
   * ```typescript
   * const guides = await client.readGuides();
   * console.log(guides['1']); // Access by character ID
   * ```
   */
  async readGuides(): Promise<Record<string, ParsedGuideWithId>> {
    console.log('Reading guides from local storage...');

    const guides: Record<string, ParsedGuideWithId> = {};

    try {
      const entries = await fs.readdir(this.guidesDir, { withFileTypes: true });

      for (const entry of entries) {
        if (entry.isFile() && entry.name.endsWith('.json')) {
          const filePath = path.join(this.guidesDir, entry.name);
          const content = await fs.readFile(filePath, 'utf-8');
          const guide = JSON.parse(content) as ParsedGuideWithId;

          // Use character ID as key if available, otherwise use character name
          const key = guide.character.id?.toString() ?? guide.character.name;
          guides[key] = guide;
        }
      }

      console.log(`✓ Read ${Object.keys(guides).length} guides`);
      return guides;
    } catch (error) {
      if ((error as NodeJS.ErrnoException).code === 'ENOENT') {
        throw new Error(
          `Guides directory not found. Run downloadGuides() first.`
        );
      }
      throw error;
    }
  }

  /**
   * Get a single guide by character name.
   * Performs case-insensitive matching if exact match is not found.
   *
   * @param characterName - The name of the character to search for
   * @returns The guide data if found, null otherwise
   *
   * @example
   * ```typescript
   * const ellenGuide = await client.getGuide('Ellen');
   * if (ellenGuide) {
   *   console.log(`Ellen guide by: ${ellenGuide.author}`);
   * }
   * ```
   */
  async getGuide(characterName: string): Promise<ParsedGuideWithId | null> {
    const guides = await this.readGuides();

    // Try to find by exact match first
    const exactMatch = Object.values(guides).find(
      g => g.character.name === characterName
    );

    if (exactMatch) return exactMatch;

    // Try case-insensitive match
    const caseInsensitiveMatch = Object.values(guides).find(
      g => g.character.name.toLowerCase() === characterName.toLowerCase()
    );

    return caseInsensitiveMatch ?? null;
  }

  /**
   * Clear all downloaded guides from local storage.
   * Removes the entire guides directory.
   *
   * @throws {Error} If the deletion fails
   *
   * @example
   * ```typescript
   * await client.clearGuides();
   * ```
   */
  async clearGuides(): Promise<void> {
    try {
      await fs.rm(this.guidesDir, { recursive: true, force: true });
      console.log('✓ Cleared all guides');
    } catch (error) {
      console.error('Error clearing guides:', error);
      throw error;
    }
  }
}
