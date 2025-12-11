from __future__ import annotations

import asyncio
import json

import anyio
import yaml

from szgf import parser
from szgf.schemas.original import OriginalGuide


async def _parse_guide(path: anyio.Path) -> None:
    content = await path.read_text(encoding="utf-8")
    yaml_content = yaml.safe_load(content)
    original_guide = OriginalGuide.model_validate(yaml_content)
    parsed_guide = await parser.parse_original_guide(original_guide)
    output_path = anyio.Path("guides/parsed") / path.name.replace(".yml", ".json")

    await output_path.parent.mkdir(parents=True, exist_ok=True)
    await output_path.write_text(
        json.dumps(parsed_guide.model_dump(), indent=2, ensure_ascii=False), encoding="utf-8"
    )


async def parse_guides() -> None:
    async with asyncio.TaskGroup() as tg:
        async for path in anyio.Path("guides/original").glob("*.yml"):
            tg.create_task(_parse_guide(path))


if __name__ == "__main__":
    asyncio.run(parse_guides())
