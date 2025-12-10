from __future__ import annotations

from enum import StrEnum
from typing import TYPE_CHECKING

import hakushin

from szgf.schemas.parsed import (
    ParsedCharacter,
    ParsedGuide,
    ParsedTeam,
    ParsedTeamMember,
    ParsedTeamSection,
    ParsedWeaponSection,
)

if TYPE_CHECKING:
    from szgf.schemas.original import (
        Character,
        DiscSection,
        DiscSetSection,
        OriginalGuide,
        Team,
        TeamMember,
        TeamSection,
        WeaponSection,
    )

SINGLE_DISC_ICON_URL = "https://raw.githubusercontent.com/seriaati/zzz-guides/refs/heads/main/assets/drive_discs/single/{id}.webp"
COMBINED_DISC_ICON_URL = "https://raw.githubusercontent.com/seriaati/zzz-guides/refs/heads/main/assets/drive_discs/combined/{id1}_{id2}.webp"


class Stat(StrEnum):
    HP = "hp"
    ATK = "atk"
    DEF = "def"
    CRIT_RATE = "cr"
    CRIT_DMG = "cd"
    ENERGY_REGEN = "er"
    IMPACT = "imp"
    ANOMALY_MASTERY = "am"
    ANOMALY_PROFICIENCY = "ap"
    PEN_RATIO = "pr"
    PEN = "pen"

    SHEER_FORCE = "sf"
    AAA = "aaa"
    """Automatic Adrenaline Accumulation"""

    ETHER_DMG_BONUS = "ether"
    PHYSICAL_DMG_BONUS = "physical"
    FIRE_DMG_BONUS = "fire"
    ICE_DMG_BONUS = "ice"
    ELECTRIC_DMG_BONUS = "elec"


STAT_KW_MATCHES = {
    Stat.HP: ("hp", "max hp", "flat hp", "hp%"),
    Stat.ATK: ("atk", "flat atk", "atk%"),
    Stat.DEF: ("def", "flat def", "def%"),
    Stat.CRIT_RATE: ("crit rate", "cr", "crit rate%", "cr%"),
    Stat.CRIT_DMG: ("crit damage", "crit dmg", "cd", "crit dmg%", "cd%"),
    Stat.ENERGY_REGEN: ("energy regen", "er"),
    Stat.IMPACT: ("impact",),
    Stat.ANOMALY_MASTERY: ("anomaly mastery", "am"),
    Stat.ANOMALY_PROFICIENCY: ("anomaly proficiency", "ap"),
    Stat.PEN_RATIO: ("pen ratio", "pen ratio%"),
    Stat.PEN: ("pen", "flat pen"),
    Stat.SHEER_FORCE: ("sheer force",),
    Stat.AAA: ("aaa", "automatic adrenaline accumulation", "adrenaline"),
    Stat.ETHER_DMG_BONUS: ("ether damage bonus", "ether dmg bonus", "ether dmg", "ether"),
    Stat.PHYSICAL_DMG_BONUS: (
        "physical damage bonus",
        "physical dmg bonus",
        "physical dmg",
        "physical",
    ),
    Stat.FIRE_DMG_BONUS: ("fire damage bonus", "fire dmg bonus", "fire dmg", "fire"),
    Stat.ICE_DMG_BONUS: ("ice damage bonus", "ice dmg bonus", "ice dmg", "ice"),
    Stat.ELECTRIC_DMG_BONUS: (
        "electric damage bonus",
        "electric dmg bonus",
        "electric dmg",
        "electric",
    ),
}


async def get_character_by_name(name: str) -> hakushin.zzz.Character | None:
    async with hakushin.HakushinAPI(hakushin.Game.ZZZ) as api:
        characters = await api.fetch_characters()
        for character in characters:
            if character.name.lower() == name.lower():
                return character
    return None


async def get_weapon_by_name(name: str) -> hakushin.zzz.Weapon | None:
    async with hakushin.HakushinAPI(hakushin.Game.ZZZ) as api:
        weapons = await api.fetch_weapons()
        for weapon in weapons:
            if weapon.name.lower() == name.lower():
                return weapon
    return None


async def get_drive_disc_by_name(name: str) -> hakushin.zzz.DriveDisc | None:
    async with hakushin.HakushinAPI(hakushin.Game.ZZZ) as api:
        drive_discs = await api.fetch_drive_discs()
        for disc in drive_discs:
            if disc.name.lower() == name.lower():
                return disc
    return None


async def _parse_character(original_character: Character) -> ParsedCharacter:
    """Parse character data from original guide."""
    character = await get_character_by_name(original_character.name)
    if character is None:
        msg = f"Character '{original_character.name}' not found in Hakushin API"
        raise ValueError(msg)

    return ParsedCharacter(
        name=character.name,
        id=character.id,
        element=character.element,
        specialty=character.specialty,
        rarity=original_character.rarity,
        banner=f"https://api.hakush.in/zzz/UI/Mindscape_{character.id}_3.webp",
    )


async def _parse_weapons(original_weapons: list[WeaponSection]) -> list:
    """Parse weapons data from original guide."""
    parsed_weapons = []

    for weapon in original_weapons:
        weapon_data = await get_weapon_by_name(weapon.name)
        if weapon_data is not None:
            parsed_weapon = ParsedWeaponSection(
                id=weapon_data.id,
                rarity=weapon_data.rarity,
                specialty=weapon_data.specialty,
                icon=weapon.icon or weapon_data.icon,
                **weapon.model_dump(exclude={"icon"}),
            )
            parsed_weapons.append(parsed_weapon)
        else:
            parsed_weapons.append(weapon)

    return parsed_weapons


async def _parse_four_piece_discs(four_pieces: list[DiscSetSection]) -> None:
    """Parse four-piece disc sections and set their icons in-place."""
    for disc_section in four_pieces:
        disc_data = await get_drive_disc_by_name(disc_section.name)
        if disc_data is None:
            msg = f"Drive disc '{disc_section.name}' not found in Hakushin API"
            raise ValueError(msg)

        disc_section.icon = SINGLE_DISC_ICON_URL.format(id=disc_data.id)


async def _parse_two_piece_discs(two_pieces: list[DiscSetSection]) -> None:
    """Parse two-piece disc sections and set their icons in-place."""
    for disc_section in two_pieces:
        disc_names = disc_section.name.split(" / ")
        disc_ids = []
        for disc_name in disc_names:
            disc_data = await get_drive_disc_by_name(disc_name)
            if disc_data is None:
                msg = f"Drive disc '{disc_name}' not found in Hakushin API"
                raise ValueError(msg)
            disc_ids.append(disc_data.id)

        if len(disc_ids) == 1:
            disc_section.icon = SINGLE_DISC_ICON_URL.format(id=disc_ids[0])
        elif len(disc_ids) == 2:
            disc_section.icon = disc_section.icon or COMBINED_DISC_ICON_URL.format(
                id1=disc_ids[0], id2=disc_ids[1]
            )
        else:
            msg = f"Drive disc section '{disc_section.name}' has an invalid number of discs ({len(disc_ids)})"
            raise ValueError(msg)


async def _parse_discs(discs_section: DiscSection | None) -> None:
    """Parse disc sections (both four-piece and two-piece) in-place."""
    if discs_section is not None:
        await _parse_four_piece_discs(discs_section.four_pieces)
        await _parse_two_piece_discs(discs_section.two_pieces)


async def _parse_team_member(member: TeamMember) -> ParsedTeamMember:
    """Parse a single team member with multiple character alternatives."""
    member_names = member.name.split(" / ")
    member_ids: list[int] = []
    member_icons: list[str] = []

    for name in member_names:
        member_data = await get_character_by_name(name)
        if member_data is None:
            msg = f"Team member '{name}' not found in Hakushin API"
            raise ValueError(msg)
        member_ids.append(member_data.id)
        member_icons.append(member_data.icon)

    return ParsedTeamMember(ids=member_ids, icons=member_icons, name=member.name)


async def _parse_team(team: Team) -> ParsedTeam:
    """Parse a single team with all its members."""
    parsed_members: list[ParsedTeamMember] = []

    for member in team.characters:
        parsed_member = await _parse_team_member(member)
        parsed_members.append(parsed_member)

    return ParsedTeam(name=team.name, characters=parsed_members, description=team.description)


async def _parse_team_section(original_team: TeamSection | None) -> ParsedTeamSection | None:
    """Parse team section with all teams."""
    if original_team is None:
        return None

    parsed_teams: list[ParsedTeam] = []

    for team in original_team.teams:
        parsed_team = await _parse_team(team)
        parsed_teams.append(parsed_team)

    return ParsedTeamSection(teams=parsed_teams, extra_sections=original_team.extra_sections)


async def parse_original_guide(original: OriginalGuide) -> ParsedGuide:
    """Parse an original guide into a parsed guide with enriched data from Hakushin API."""
    parsed_character = await _parse_character(original.character)
    parsed_weapons = await _parse_weapons(original.weapons)
    await _parse_discs(original.discs)
    parsed_team_section = await _parse_team_section(original.team)

    return ParsedGuide(
        character=parsed_character,
        weapons=parsed_weapons,
        team=parsed_team_section,
        **original.model_dump(exclude={"character", "weapons", "team"}),
    )
