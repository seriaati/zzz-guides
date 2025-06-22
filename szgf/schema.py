from enum import StrEnum
from typing import Literal
import pydantic


class Section(pydantic.BaseModel):
    """A section, anything can be written, like additional explanations."""

    title: str
    description: str


class Character(pydantic.BaseModel):
    name: str
    rarity: Literal[4, 5]

    banner: str | None = None
    """A custom banner can be provided, otherwise defaults to M6 art."""


class WeaponSection(pydantic.BaseModel):
    name: str
    description: str

    title: str | None = None
    """A custom title for the section can be provided, otherwise shows
       the ranking of the weapon, e.g. "2nd Best W-Engine."""
    icon: str | None = None
    """A custom icon can be provided, otherwise an icon will be fetched based on the name."""


class RelicSetSection(pydantic.BaseModel):
    name: str
    description: str

    icon: str | None = None
    """A custom icon can be provided, otherwise an icon will be fetched based on the name."""


class RelicSection(pydantic.BaseModel):
    four_pieces: list[RelicSetSection]
    two_pieces: list[RelicSetSection]
    extra_sections: list[Section]


class RelicMainStatSection(pydantic.BaseModel):
    stat_priority: str
    pos: Literal[4, 5, 6]


class RelicStatSection(pydantic.BaseModel):
    main_stats: list[RelicMainStatSection]
    sub_stats: str
    baseline_stats: str

    extra_sections: list[Section] = pydantic.Field(default_factory=list)


class MindscapeSection(pydantic.BaseModel):
    num: Literal[1, 2, 3, 4, 5, 6]
    description: str


class SkillType(StrEnum):
    CORE = "core"
    BASIC = "basic"
    DODGE = "dodge"
    SPECIAL = "special"
    CHAIN = "chain"
    ASSIST = "assist"


class SkillPrioritySection(pydantic.BaseModel):
    priorities: list[list[SkillType]]
    description: str

    @pydantic.field_validator("priorities")
    def __convert_priorities(cls, v: list[str]) -> list[list[SkillType]]:
        return [[SkillType(skill) for skill in priority.split(",")] for priority in v]


class TeamMember(pydantic.BaseModel):
    name: str


class Team(pydantic.BaseModel):
    name: str
    characters: list[TeamMember]
    description: str | None = None


class TeamSection(pydantic.BaseModel):
    teams: list[Team]
    extra_sections: list[Section] = pydantic.Field(default_factory=list)


class Skill(pydantic.BaseModel):
    title: str
    description: str
    explanation: str
    demo: str | None = None


class Guide(pydantic.BaseModel):
    character: Character
    description: str

    weapons: list[WeaponSection] = pydantic.Field(default_factory=list)
    relics: list[RelicSection] = pydantic.Field(default_factory=list)
    stat: RelicStatSection | None = None
    skill_priority: SkillPrioritySection | None = None
    skills: list[Skill] = pydantic.Field(default_factory=list)
    mindscapes: list[MindscapeSection] = pydantic.Field(default_factory=list)
    team: TeamSection | None = None
