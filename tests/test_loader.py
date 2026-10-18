from heavy_equipment_search.loader import parse_price


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
