# Contribution Guidelines

## Getting Started

You can check existing guides by using the `/build zzz` command in Hoyo Buddy.

Use the [SZGF generator](https://generator.szgf.seria.moe) to write your guide using a user-friendly interface. The generator will help you create a valid guide file.

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

Alternatively, you can use `|-` to preserve line breaks exactly as written. Example:

```yaml
description: |-
  This is a long sentence that
  spans multiple lines in the YAML file,
  and will be rendered with line breaks preserved.
```

Renders as:

```txt
This is a long sentence that
spans multiple lines in the YAML file,
and will be rendered with line breaks preserved.
```
