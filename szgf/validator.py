from __future__ import annotations

from typing import Any

from szgf.schema import Guide


def validate_szgf(data: Any) -> Guide:
    return Guide.model_validate(data)
