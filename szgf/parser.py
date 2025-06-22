from typing import Any

from szgf.schema import Guide


def parse_szgf(data: Any) -> Guide:
    return Guide.model_validate(data)
