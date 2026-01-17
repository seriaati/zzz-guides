# zzz-guides

- [Official website](https://szgf.seria.moe)
- [Documentation](https://docs.szgf.seria.moe)
- [Generator](https://generator.szgf.seria.moe)
- [Discord server](https://link.seria.moe/hb-dc)

## About

SZGF stands for Standardized Zenless Zone Zero Guide Format, a YAML-based format for writing guides for agents in Zenless Zone Zero.

You can see it in action in the [Hoyo Buddy](https://hb.seria.moe) Discord bot.

This repository contains:

- `/guides`: SZGF guide files.
- `/schema.json`: SZGF JSON schema file.
- `/szgf`: Python SDK.
- `/assets`: Drive disc, stats, and UI icons.
- `/docs`: Documentation and contribution guidelines.

## Python SDK

You can use the SZGF Python SDK to download and read guides from this repository. The guides will be parsed using Pydantic and available as Python objects.

Install the package:

```bash
pip install szgf
```

Import and use the `SZGFClient` to fetch and read guides:

```python
from szgf.client import SZGFClient
client = SZGFClient()
await client.download_guides()
guides = await client.read_guides() # Returns a dict of ParsedGuide objects
```

## Contributing

See [CONTRIBUTING.md](https://docs.szgf.seria.moe/CONTRIBUTING/) for contribution guidelines.
