from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import requests

CHARACTERS_API_URL: Final[str] = "https://api.hakush.in/zzz/data/character.json"


@dataclass
class Character:
    name: str
    id: int


def get_characters() -> list[Character]:
    response = requests.get(CHARACTERS_API_URL, timeout=5)
    data = response.json()
    return [Character(name=c["EN"], id=cid) for cid, c in data.items()]
