from heavy_equipment_search.loader import normalize_brand, parse_price


def test_dollar_price():
    result = parse_price("$85,000")
    assert result == 85000.0


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


def test_normalize_brand_known():
    result = normalize_brand("cat ")
    assert result == "Caterpillar"


def test_normalize_brand_unknown():
    result = normalize_brand("XCMG")
    assert result == "XCMG"


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
