# Python SDK

## Installation

```bash
pip install szgf
```

## Usage

```python
from szgf.client import SZGFClient

client = SZGFClient()
await client.download_guides()
guides = await client.read_guides()
print(guides['1011']) # Anby
```
