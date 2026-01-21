const path = require('path');
const fs = require('fs').promises;

// Resolve module from szgf-ts directory
const modulePath = path.join(__dirname, '..', 'szgf-ts', 'node_modules', 'json-schema-to-typescript');
const { compileFromFile } = require(modulePath);

async function generateTypes() {
  try {
    const schemaPath = path.join(__dirname, '..', 'schema.json');
    const outputPath = path.join(__dirname, '..', 'szgf-ts', 'src', 'types.ts');

    console.log('Generating TypeScript types from schema.json...');

    const ts = await compileFromFile(schemaPath, {
      bannerComment: '/* eslint-disable */\n/**\n * This file was automatically generated from schema.json.\n * DO NOT MODIFY IT BY HAND. Instead, modify the source Pydantic models,\n * regenerate schema.json, and run this script again.\n */',
      unknownAny: false,
      strictIndexSignatures: true,
    });

    await fs.writeFile(outputPath, ts, 'utf-8');
    console.log('✓ TypeScript types generated successfully at:', outputPath);
  } catch (error) {
    console.error('Error generating TypeScript types:', error);
    process.exit(1);
  }
}

generateTypes();
