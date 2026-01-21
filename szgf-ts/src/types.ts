/* eslint-disable */
/**
 * This file was automatically generated from schema.json.
 * DO NOT MODIFY IT BY HAND. Instead, modify the source Pydantic models,
 * regenerate schema.json, and run this script again.
 */

/**
 * Author of the guide
 */
export type Author = string;
/**
 * Last updated date of the guide
 */
export type LastUpdated = string;
/**
 * Name of the character
 */
export type Name = string;
/**
 * Rarity of the character, either 4 (A-rank) or 5 (S-rank) stars.
 */
export type Rarity = 4 | 5;
/**
 * Banner image for the character
 */
export type Banner = string | null;
/**
 * Description of the guide, explaining its purpose and content.
 */
export type Description = string;
/**
 * Name of the weapon
 */
export type Name1 = string;
/**
 * Description of the weapon
 */
export type Description1 = string;
/**
 * Title of the section. A custom title for the section can be provided, otherwise shows the ranking of the weapon, e.g. '2nd Best W-Engine.'
 */
export type Title = string | null;
/**
 * Icon of the weapon. A custom icon can be provided, otherwise an icon will be fetched based on the name.
 */
export type Icon = string | null;
/**
 * List of weapon sections for the character.
 */
export type Weapons = WeaponSection[];
/**
 * Name of the drive disc set
 */
export type Name2 = string;
/**
 * Description for this section
 */
export type Description2 = string;
/**
 * Icon of the drive disc set. A custom icon can be provided, otherwise an icon will be fetched based on the name.
 */
export type Icon1 = string | null;
/**
 * List of four-piece disc sets.
 */
export type FourPieces = DiscSetSection[];
/**
 * List of two-piece disc sets.
 */
export type TwoPieces = DiscSetSection[];
/**
 * Title of the section
 */
export type Title1 = string;
/**
 * Description of the section
 */
export type Description3 = string;
/**
 * Additional sections that can be added to the disc section.
 */
export type ExtraSections = Section[];
/**
 * Priority of the main stat for this position's disc, e.g. 'ATK > CRIT DMG > CRIT RATE'.
 */
export type StatPriority = string;
/**
 * Position of the disc, either 4, 5, or 6.
 */
export type Pos = 4 | 5 | 6;
/**
 * List of main stats for each disc position (4, 5, 6).
 */
export type MainStats = DiscMainStatSection[];
/**
 * Priority of sub stats for the character, e.g. 'ATK > CRIT DMG > CRIT RATE > SPD'.
 */
export type SubStats = string;
/**
 * Baseline stats for the character, e.g. 'ATK: 1000, DEF: 500, HP: 2000'.
 */
export type BaselineStats = string;
/**
 * Additional sections that can be added to the stat section.
 */
export type ExtraSections1 = Section[];
/**
 * Types of skills in ZZZ.
 */
export type SkillType = "core" | "basic" | "dodge" | "special" | "chain" | "assist";
/**
 * List of skill priorities, where each sublist represents a priority level. For example, [[core, basic], [special, dodge]] means the first priority is core and basic skills, and the second priority is special and dodge skills.
 */
export type Priorities = SkillType[][];
/**
 * Description of the skill priority section
 */
export type Description4 = string | null;
/**
 * Title of the skill
 */
export type Title2 = string;
/**
 * Description of the skill
 */
export type Description5 = string;
/**
 * Explanation of the skill mechanics
 */
export type Explanation = string;
/**
 * Demo GIF of the skill
 */
export type Demo = string | null;
/**
 * List of skills for the character.
 */
export type Skills = Skill[];
/**
 * Number of the mindscape, from 1 to 6.
 */
export type Num = 1 | 2 | 3 | 4 | 5 | 6;
/**
 * Description of the mindscape, explaining its effects and importance.
 */
export type Description6 = string;
/**
 * List of mindscapes for the character.
 */
export type Mindscapes = MindscapeSection[];
/**
 * Name of the team
 */
export type Name3 = string;
/**
 * Name of the team member
 */
export type Name4 = string;
/**
 * List of characters in the team
 */
export type Characters = TeamMember[];
/**
 * Description of the team
 */
export type Description7 = string | null;
/**
 * List of teams that the character can be part of.
 */
export type Teams = Team[];
/**
 * Additional sections for the team section.
 */
export type ExtraSections2 = Section[];

/**
 * The standardized ZZZ guide format (SZGF) schema.
 */
export interface OriginalGuide {
  author: Author;
  last_updated: LastUpdated;
  character: Character;
  description: Description;
  weapons?: Weapons;
  /**
   * Disc section for the character.
   */
  discs?: DiscSection | null;
  /**
   * Stat section for the character.
   */
  stat?: StatSection | null;
  /**
   * Skill priority section for the character.
   */
  skill_priority?: SkillPrioritySection | null;
  skills?: Skills;
  mindscapes?: Mindscapes;
  /**
   * Team section for the character.
   */
  team?: TeamSection | null;
  /**
   * Rotation section for the character, explaining how to use skills effectively.
   */
  rotation?: Section | null;
  [k: string]: any | undefined;
}
/**
 * Character information
 */
export interface Character {
  name: Name;
  rarity: Rarity;
  banner?: Banner;
  [k: string]: any | undefined;
}
/**
 * A weapon section for a character.
 */
export interface WeaponSection {
  name: Name1;
  description: Description1;
  title?: Title;
  icon?: Icon;
  [k: string]: any | undefined;
}
/**
 * A drive disc section for a character.
 */
export interface DiscSection {
  four_pieces: FourPieces;
  two_pieces: TwoPieces;
  extra_sections?: ExtraSections;
  [k: string]: any | undefined;
}
/**
 * A drive disc set section.
 */
export interface DiscSetSection {
  name: Name2;
  description: Description2;
  icon?: Icon1;
  [k: string]: any | undefined;
}
/**
 * A section, anything can be written, like additional explanations.
 */
export interface Section {
  title: Title1;
  description: Description3;
  [k: string]: any | undefined;
}
/**
 * Stat section for a character.
 */
export interface StatSection {
  main_stats: MainStats;
  sub_stats: SubStats;
  baseline_stats: BaselineStats;
  extra_sections?: ExtraSections1;
  [k: string]: any | undefined;
}
/**
 * Main stat section for a drive disc.
 */
export interface DiscMainStatSection {
  stat_priority: StatPriority;
  pos: Pos;
  [k: string]: any | undefined;
}
/**
 * Skill priority section for a character.
 */
export interface SkillPrioritySection {
  priorities: Priorities;
  description?: Description4;
  [k: string]: any | undefined;
}
/**
 * A skill of a character.
 */
export interface Skill {
  title: Title2;
  description: Description5;
  explanation: Explanation;
  demo?: Demo;
  [k: string]: any | undefined;
}
/**
 * A mindscape cinema section for a character.
 */
export interface MindscapeSection {
  num: Num;
  description: Description6;
  [k: string]: any | undefined;
}
/**
 * Team section for a character.
 */
export interface TeamSection {
  teams?: Teams;
  extra_sections?: ExtraSections2;
  [k: string]: any | undefined;
}
/**
 * A team that a character can be part of.
 */
export interface Team {
  name: Name3;
  characters: Characters;
  description?: Description7;
  [k: string]: any | undefined;
}
/**
 * A team member in a team.
 */
export interface TeamMember {
  name: Name4;
  [k: string]: any | undefined;
}
