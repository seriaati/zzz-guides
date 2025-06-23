# zzz-guides

This repository contains ZZZ agent guides and the definition of Standardized ZZZ Guide Format (SZGF).

## Terminology

For consistency, the following terms are used throughout the repository:

- Character: ZZZ agent.
- Weapon: W-engine.
- Rarity: ZZZ agent or weapon rarity (S: 5, A: 4, B: 3)

## Formatting

The `description` and `explanation` fields accept Markdown formatting. See Discord's [Markdown guide](https://support.discord.com/hc/en-us/articles/210298617) for details.

## Contributing

If you're unfamiliar with Git on the command line, you can use [GitHub Desktop](https://desktop.github.com/).

1. Make a fork of this repository.
1. Create a new branch for your changes (e.g. `nicole-guide`).
1. Create a new file in the `guides/original` directory with the name of the character (e.g. `nicole.md`).
1. At the top of the file, add the schema:

   ```yml
   # yaml-language-server: $schema=https://raw.githubusercontent.com/seriaati/zzz-guides/refs/heads/main/schema.json
   ```

1. Write your guide in the file using the Standardized ZZZ Guide Format (SZGF). You can refer to existing guides in the `guides/original` directory for examples.
1. Push your changes to your fork.
1. Create a pull request to the main repository.
