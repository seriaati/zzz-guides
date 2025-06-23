from __future__ import annotations

from pathlib import Path

import yaml
from loguru import logger
from pydantic import ValidationError

from szgf.validator import validate_szgf


def validate_original_guides() -> None:
    for file_path in Path("guides/original").glob("*.yml"):
        with file_path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

            try:
                validate_szgf(data)
            except ValidationError:
                logger.error(f"Validation failed for {file_path.name}")
                raise


if __name__ == "__main__":
    validate_original_guides()
