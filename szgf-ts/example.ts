import { SZGFClient } from './src';

async function main() {
  // Create a client instance
  const client = new SZGFClient();

  // Download guides from GitHub
  await client.downloadGuides();

  // Read all guides
  const guides = await client.readGuides();
  console.log(`Loaded ${Object.keys(guides).length} guides`);

  // Get a specific guide by character name
  const ellenGuide = await client.getGuide('Ellen');
  if (ellenGuide) {
    console.log(`Ellen guide by: ${ellenGuide.author}`);
    console.log(`Weapons: ${ellenGuide.weapons.length}`);
  }
}

main().catch(console.error);
