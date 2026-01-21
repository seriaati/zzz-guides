# TypeScript SDK

## Installation

```bash
npm install szgf
```

## Usage

```typescript
import { SZGFClient } from 'szgf';

const client = new SZGFClient();
await client.downloadGuides();
const guides = await client.readGuides();
console.log(guides['1011']); // Anby
const anbyGuide = await client.getGuide('Anby');
await client.clearGuides();
```
