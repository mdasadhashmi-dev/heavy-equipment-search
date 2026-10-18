"""Load and clean heavy-equipment listings."""


def parse_price(raw):
    if raw is None:
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
    if raw_brand is None:
        return None
    cleaned = raw_brand.strip()
    if not cleaned:
        return None
    key = cleaned.lower()
    return BRAND_ALIASES.get(key, cleaned)
