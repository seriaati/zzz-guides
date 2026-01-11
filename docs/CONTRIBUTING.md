# Contribution Guidelines

## Getting Started

Unfortunately,

### For Non-Technical People

1. Read the [Standardized ZZZ Guide Format (SZGF) documentation](schema.json) to understand the required fields and structure.

### For Technical People

If you're unfamiliar with Git on the command line, you can use [GitHub Desktop](https://desktop.github.com/).

1. [Make a fork of this repository.](https://github.com/seriaati/zzz-guides/fork)
1. Create a new branch for your changes (e.g. `nicole-guide`).
1. Create a new file in the `guides/original` directory with the name of the character (e.g. `nicole.yml`).
1. At the top of the file, add the schema:

   ```yml
   # yaml-language-server: $schema=../../schema.json
   ```

1. Write your guide in the file using the Standardized ZZZ Guide Format (SZGF). You can refer to existing guides in the `guides/original` directory for examples.
1. Push your changes to your fork.
1. Create a pull request to the main repository.
1. If you are not the author of the original guide, include a link to it in the pull request description, along with any additional context or notes about your changes.
1. Wait for the maintainers to review your pull request. We may request changes or provide feedback.

## Formatting

### Markdown

The `description` and `explanation` fields accept Markdown formatting. See Discord's [Markdown guide](https://support.discord.com/hc/en-us/articles/210298617) for details.

### UI Buttons

In the skill section, you might need to reference UI buttons. Use the following format:

| Image | UI Button Name | Tag |
| :---: | :---: | :---: |
| ![Basic Attack](https://api.hakush.in/zzz/UI/Icon_Normal.webp) | Basic Attack | `<basic>` |
| ![Dodge](https://api.hakush.in/zzz/UI/Icon_Evade.webp) | Dodge | `<dodge>` |
| ![Chain](https://api.hakush.in/zzz/UI/Icon_UltimateReady.webp) | Chain | `<chain>` |
| ![Special](https://api.hakush.in/zzz/UI/Icon_SpecialReady.webp) | Special | `<special>` |
| ![Assist](https://api.hakush.in/zzz/UI/Icon_Switch.webp) | Assist | `<assist>` |
| ![Core Skill](https://api.hakush.in/zzz/UI/Icon_CoreSkill.webp) | Core Skill | `<core>` |

Example:

```yaml
skill:
  - name: "Assist Follow-Up: Hammer Bell"
    description: |
      Press <basic> after a Defensive Assist to activate. Koleda charges and strikes enemies in front, dealing Fire DMG and obtaining Furnace Fire effect.
    explanation: |
      Use this skill after a Defensive Assist to deal damage and gain Furnace Fire, which increases your damage output.
```

## Terminology

For consistency, the following terms are used throughout the repository:

- Character: ZZZ agent.
- Weapon: W-engine.
- Rarity: ZZZ agent or weapon rank (S-rank: 5, A-rank: 4, B-rank: 3)
