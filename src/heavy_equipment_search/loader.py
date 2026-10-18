"""Load and clean heavy-equipment listings."""

import pandas as pd


def parse_price(raw):
    if pd.isna(raw):
        return None
    try:
        if isinstance(raw, (int, float)):
            return float(raw)
        raw = raw.upper()
        cleaned = raw.replace("$", "").replace(",", "").replace("USD", "").strip()
        return float(cleaned) if cleaned else None
    except ValueError:
        return None


BRAND_ALIASES = {
    "cat": "Caterpillar",
    "caterpillar": "Caterpillar",
    "komatsu": "Komatsu",
    "volvo": "Volvo",
    "jcb": "JCB",
    "hitachi": "Hitachi",
    "liebherr": "Liebherr",
}


def normalize_brand(raw_brand):
    if pd.isna(raw_brand):
        return None
    cleaned = raw_brand.strip()
    if not cleaned:
        return None
    key = cleaned.lower()
    return BRAND_ALIASES.get(key, cleaned)


def parse_hours(raw):
    if pd.isna(raw):
        return None
    try:
        if isinstance(raw, (int, float)):
            return float(raw)
        raw = raw.upper()
        cleaned = raw.replace("HRS", "").replace(",", "").replace("HOURS", "").strip()
        return float(cleaned) if cleaned else None
    except ValueError:
        return None
