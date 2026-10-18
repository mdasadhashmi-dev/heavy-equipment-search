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
