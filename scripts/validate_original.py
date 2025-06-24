from __future__ import annotations

from pathlib import Path

import jsonschema
import pydantic
import yaml
from loguru import logger

from szgf.validator import validate_szgf


def validate_with_pydantic() -> None:
    for file_path in Path("guides/original").glob("*.yml"):
        logger.info(f"Validating {file_path.name} against Pydantic")

        with file_path.open("r", encoding="utf-8") as file:
            try:
                data = yaml.safe_load(file)
            except yaml.YAMLError as e:
                logger.error(f"YAML parsing error in {file_path.name}: {e}")
                raise

            try:
                validate_szgf(data)
            except pydantic.ValidationError:
                logger.error(f"Validation failed for {file_path.name}")
                raise


def validate_with_jsonschema() -> None:
    schema_path = Path("schema.json")
    with schema_path.open("r", encoding="utf-8") as schema_file:
        schema = yaml.safe_load(schema_file)

    for file_path in Path("guides/original").glob("*.yml"):
        logger.info(f"Validating {file_path.name} against JSON schema")

        with file_path.open("r", encoding="utf-8") as file:
            try:
                data = yaml.safe_load(file)
            except yaml.YAMLError as e:
                logger.error(f"YAML parsing error in {file_path.name}: {e}")
                raise

            try:
                jsonschema.validate(instance=data, schema=schema)
            except jsonschema.ValidationError as e:
                logger.error(f"Validation failed for {file_path.name}: {e.message}")
                raise


if __name__ == "__main__":
    validate_with_pydantic()
    validate_with_jsonschema()
