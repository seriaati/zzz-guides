# Contribution Guidelines

## Getting Started

1. Read the [schema documentation](./schema.md) to understand the available fields and structure of SZGF.
2. Review existing guides in [`guides/original`](https://github.com/seriaati/zzz-guides/tree/main/guides/original) for examples.
3. Follow the steps below based on your technical background.

### For Non-Technical People

Use the [YAML Generator](https://gh.seria.moe/zzz-guides/form-generator.html), an AI-made website that helps you create YAML files without needing to understand the syntax.

After you're done, submit your guide by creating an issue in this repository and attaching the YAML file, or by sending it to the #submit-guides channel in our [Discord server](https://link.seria.moe/hb-dc).

### For Technical People

To proceed with this section, you need a basic understanding of Git and GitHub.

If you're using VSCode, install the [YAML extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) for schema validation and autocompletion.

1. [Make a fork of this repository](https://github.com/seriaati/zzz-guides/fork).
2. Git clone your fork locally
3. Create a new branch for your changes (e.g. `nicole-guide`).
4. Create a new file in the `guides/original` directory with the name of the character (e.g. `nicole.yml`).
5. At the top of the file, add the schema:

   ```yml
   # yaml-language-server: $schema=../../schema.json
   ```

6. Write your guide in the file.
7. Push the changes to your fork.
8. Create a pull request to the main repository.
9. If you are not the author of the original guide, include a link to it in the pull request description, along with any additional context or notes about your changes.
10. Wait for the maintainers to review your pull request. We may request changes or provide feedback.

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
    description: >-
      Press <basic> after a Defensive Assist to activate. Koleda charges and strikes enemies in front, dealing Fire DMG and obtaining Furnace Fire effect.
    explanation: >-
      Use this skill after a Defensive Assist to deal damage and gain Furnace Fire, which increases your damage output.
```

## Terminology

For consistency, the following terms are used throughout the repository:

- Character: ZZZ agent.
- Weapon: W-engine.
- Rarity: ZZZ agent or weapon rank (S-rank: 5, A-rank: 4, B-rank: 3)

## Multi-line Text

For multi-line text in fields like `description` or `explanation`, use the `>-` YAML syntax to preserve new lines. Example:

```yaml
description: >-
  This is a long sentence that
  spans multiple lines in the YAML file,
  but will be rendered as a single paragraph.

  An empty line indicates a new paragraph.
```

Renders as:

```txt
This is a long sentence that spans multiple lines in the YAML file, but will be rendered as a single paragraph.

An empty line indicates a new paragraph.
```
