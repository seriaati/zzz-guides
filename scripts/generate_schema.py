from __future__ import annotations

import json
from pathlib import Path

from szgf.schema import Guide


def generate_schema() -> None:
    schema = Guide.model_json_schema()
    with Path("schema.json").open("w", encoding="utf-8") as file:
        json.dump(schema, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    generate_schema()
    print("Schema generated successfully.")
