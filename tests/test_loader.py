from pathlib import Path

import pandas as pd

from heavy_equipment_search.loader import (
    load_listings,
    normalize_brand,
    parse_hours,
    parse_price,
)

DATA_FILE = Path(__file__).parent.parent / "data" / "listings.csv"


#### Price #####
def test_poa_price():
    result = parse_price("POA")
    assert result is None


def test_usd_price():
    result = parse_price("usd 78500")
    assert result == 78500.0


def test_numeric_price():
    result = parse_price(85000)
    assert result == 85000.0


def test_none_price():
    result = parse_price(None)
    assert result is None


def test_invalid_price():
    result = parse_price("invalid")
    assert result is None


def test_empty_string_price():
    result = parse_price("")
    assert result is None


def test_price_with_spaces():
    result = parse_price("  $  85,000  ")
    assert result == 85000.0


def test_price_with_usd_and_spaces():
    result = parse_price("  USD  85,000  ")
    assert result == 85000.0


def test_price_with_lowercase_usd():
    result = parse_price("usd 85,000")
    assert result == 85000.0


def test_price_with_mixed_case_usd():
    result = parse_price("UsD 85,000")
    assert result == 85000.0


def test_price_nan():
    result = parse_price(float("nan"))
    assert result is None


def test_normalize_brand_known():
    result = normalize_brand("cat ")
    assert result == "Caterpillar"


def test_normalize_brand_unknown():
    result = normalize_brand("XCMG")
    assert result == "XCMG"


def test_normalize_brand_nan():
    result = normalize_brand(float("nan"))
    assert result is None


#######Brand###########
def test_normalize_brand_none():
    result = normalize_brand(None)
    assert result is None


def test_normalize_brand_empty_string():
    result = normalize_brand("")
    assert result == None


def test_normalize_brand_whitespace():
    result = normalize_brand("   ")
    assert result == None


def test_normalize_brand_case_insensitive():
    result = normalize_brand("CATERPILLAR")
    assert result == "Caterpillar"


def test_normalize_brand_alias():
    result = normalize_brand("jcb")
    assert result == "JCB"


def test_normalize_brand_alias_with_spaces():
    result = normalize_brand("  jcb  ")
    assert result == "JCB"


def test_normalize_brand_alias_with_mixed_case():
    result = normalize_brand("JcB")
    assert result == "JCB"


def test_normalize_brand_alias_with_mixed_case_and_spaces():
    result = normalize_brand("  JcB  ")
    assert result == "JCB"


def test_normalize_brand_unknown_with_spaces():
    result = normalize_brand("  XCMG ")
    assert result == "XCMG"


def test_normalize_nan():
    result = normalize_brand(float("nan"))
    assert result is None


#####Hours Parsing Tests #####


def test_parse_hours_with_comma():
    result = parse_hours("1,234")
    assert result == 1234.0


def test_parse_hours_with_spaces():
    result = parse_hours("  1,234  ")
    assert result == 1234.0


def test_parse_hours_poa():
    result = parse_hours("POA")
    assert result is None


def test_parse_hours_none():
    result = parse_hours(None)
    assert result is None


def test_parse_hours_invalid():
    result = parse_hours("invalid")
    assert result is None


def test_parse_hours_empty_string():
    result = parse_hours("")
    assert result is None


def test_parse_hours_only_spaces():
    result = parse_hours("  ")
    assert result is None


def test_parse_hours_with_decimal():
    result = parse_hours("1234.56")
    assert result == 1234.56


def test_parse_hours_with_comma_and_decimal():
    result = parse_hours("1,234.56")
    assert result == 1234.56


def test_parse_hours_without_comma():
    result = parse_hours("1234")
    assert result == 1234.0


def test_parse_hours_with_invalid_characters():
    result = parse_hours("1,`234")
    assert result is None


def test_parse_hours_with_hrs_unit():
    result = parse_hours("6200 hrs")
    assert result == 6200.0


def test_parse_hours_with_uppercase_unit_and_comma():
    result = parse_hours("6,200 HRS")
    assert result == 6200.0


def test_parse_hours_with_full_word_unit():
    result = parse_hours("6200 hours")
    assert result == 6200.0


def test_parse_hours_already_a_number():
    result = parse_hours(5900)
    assert result == 5900.0


def test_parse_hours_nan():
    result = parse_hours(float("nan"))
    assert result is None


### Load listings ####


def test_load_listings_remove_duplicates():
    df = load_listings(DATA_FILE)
    assert df.shape[0] == 11  # Expecting 11 rows after removing duplicates


def test_load_listings_columns():
    df = load_listings(DATA_FILE)
    expected_columns = [
        "listing_id",
        "title",
        "brand",
        "model",
        "year",
        "hours",
        "location",
        "description",
        "price_usd",
    ]
    assert all(col in df.columns for col in expected_columns)
    assert "price" not in df.columns  # Ensure the original price column is removed


def test_load_listings_dtypes():
    df = load_listings(DATA_FILE)
    assert pd.api.types.is_float_dtype(df["price_usd"])
    assert pd.api.types.is_float_dtype(df["hours"])
    assert str(df["year"].dtype) == "Int64"


def test_load_listings_brand_normalization():
    df = load_listings(DATA_FILE)
    assert (
        df["brand"]
        .isin(["Caterpillar", "Komatsu", "Volvo", "JCB", "Hitachi", "Liebherr"])
        .all()
    )


def test_load_listings_duplicate_gone():
    df = load_listings(DATA_FILE)
    assert (
        "1011" not in df["listing_id"].tolist()
    )  # Ensure the duplicate listing is removed


##test for every brand is canonical##


def test_load_listings_all_brands_canonical():
    df = load_listings(DATA_FILE)
    assert set(df["brand"]) <= {
        "Caterpillar",
        "Komatsu",
        "Volvo",
        "JCB",
        "Hitachi",
        "Liebherr",
        "XCMG",
    }
