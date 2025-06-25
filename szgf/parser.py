from __future__ import annotations

from enum import StrEnum


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


KW_MATCHES = {
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
