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


def load_listings(path):
    """Read the listings CSV and return a cleaned DataFrame."""
    import pandas as pd

    # 1. Read the CSV with every column as text
    df = pd.read_csv("data/listings.csv", dtype=str)

    # 2. Create price_usd from price; clean hours and brand in place
    df["price_usd"] = df["price"].map(parse_price)
    df["hours"] = df["hours"].map(parse_hours)
    df["brand"] = df["brand"].map(normalize_brand)

    # 3. Convert year to the Int64 type
    df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")

    # 4. Drop duplicate listings (compare every column except listing_id)
    content_cols = [col for col in df.columns if col != "listing_id"]

    df[df.duplicated(subset=content_cols, keep=False)]
    df = df.drop_duplicates(subset=content_cols).reset_index(drop=True)

    # 5. Drop the raw price column and renumber the rows
    df = df.drop(columns=["price"]).reset_index(drop=True)

    # 6. Return the cleaned DataFrame
    return df
