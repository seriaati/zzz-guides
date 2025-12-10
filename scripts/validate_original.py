from __future__ import annotations

import sys
from pathlib import Path

import jsonschema
import pydantic
import yaml
import yaml.scanner

from szgf.validator import validate_original_guide


def _parse_yaml(file_path: Path) -> dict:
    """Parse a YAML file and return its content as a dictionary."""
    with file_path.open("r", encoding="utf-8") as file:
        try:
            return yaml.safe_load(file)
        except yaml.scanner.ScannerError as e:
            mark = e.problem_mark
            if mark is not None:
                print(
                    f"::error file={file_path},line={mark.line + 1},col={mark.column + 1}::YAML parsing error"
                )
            else:
                print(f"::error file={file_path}::YAML parsing error")
            raise
        except yaml.MarkedYAMLError as e:
            mark = e.problem_mark
            if mark is not None:
                print(
                    f"::error file={file_path},line={mark.line + 1},col={mark.column + 1}::YAML parsing error"
                )
            else:
                print(f"::error file={file_path}::YAML parsing error")
            raise
        except yaml.YAMLError:
            print(f"::error file={file_path}::YAML parsing error")
            raise


def validate_with_pydantic() -> None:
    for file_path in Path("guides/original").glob("*.yml"):
        data = _parse_yaml(file_path)

        try:
            validate_original_guide(data)
        except pydantic.ValidationError as e:
            print(f"::error file={file_path.name},title=Pydantic validation failed::{e}")
            raise


def validate_with_jsonschema() -> None:
    schema_path = Path("schema.json")
    with schema_path.open("r", encoding="utf-8") as schema_file:
        schema = yaml.safe_load(schema_file)

    for file_path in Path("guides/original").glob("*.yml"):
        data = _parse_yaml(file_path)

        try:
            jsonschema.validate(instance=data, schema=schema)
        except jsonschema.ValidationError as e:
            print(f"::error file={file_path.name},title=JSON schema validation failed::{e.message}")
            raise


if __name__ == "__main__":
    try:
        validate_with_pydantic()
        validate_with_jsonschema()
    except Exception:
        sys.exit(1)
