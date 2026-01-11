# zzz-guides

This repository contains:

- ZZZ agent guides in `/guides/original`
- Parsed version of the guides in `/guides/parsed`
- Translated guides in `/guides/translated` (WIP)
- Definition of the Standardized ZZZ Guide Format (SZGF) in `/schema.json` (or as Pydantic models in `/szgf/schemas`)
- Python package for validating and fetching guides from this repository in `/szgf`
- Assets/icons used in the guides in `/assets`
- [Documentation](https://gh.seria.moe/zzz-guides/) on how to contribute and the SZGF schema

## Usage

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

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.
