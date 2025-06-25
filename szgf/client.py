from __future__ import annotations

from pathlib import Path
from typing import Literal, Self

import aiofiles
import aiofiles.os
import aiohttp
import yaml
from loguru import logger
from yarl import URL


class SZGFClient:
    def __init__(self) -> None:
        self._session: aiohttp.ClientSession | None = None
        self._guides_url = URL("https://api.github.com/repos/seriaati/zzz-guides/contents/guides")
        self._guides_dir = Path(".zzz_guides/")

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None:
            msg = "Client session has not been started. Use 'await start()' first."
            raise RuntimeError(msg)
        return self._session

    async def __aenter__(self) -> Self:
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:  # noqa: ANN001
        await self.close()

    async def _fetch_txt(self, url: URL | str) -> str:
        logger.debug(f"Fetching text from {url}")

        async with self.session.get(url) as response:
            response.raise_for_status()
            return await response.text()

    @staticmethod
    def _parse_yaml(content: str) -> dict:
        return yaml.safe_load(content)

    async def download_guides(self, guide_type: Literal["original", "parsed"]) -> None:
        logger.info(f"Downloading guides of type: {guide_type!r}")

        async with self.session.get(self._guides_url / guide_type) as response:
            response.raise_for_status()
            data = await response.json()

        await aiofiles.os.makedirs(self._guides_dir / guide_type, exist_ok=True)

        for item in data:
            if item["type"] == "file" and item["name"].endswith(".yml"):
                file_url = item["download_url"]
                content = await self._fetch_txt(file_url)

                async with aiofiles.open(
                    self._guides_dir / guide_type / item["name"], mode="w", encoding="utf-8"
                ) as file:
                    await file.write(content)

    async def start(self) -> None:
        self._session = aiohttp.ClientSession()

    async def close(self) -> None:
        if self._session is not None:
            await self._session.close()
