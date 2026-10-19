from pydantic import ValidationError
import pytest

from heavy_equipment_search.models import Listing


def test_listing_rejects_missing_title():
    with pytest.raises(ValidationError):
        Listing(
            listing_id="1001",
            price_usd=85000.0,
            year=2018,
            brand="Caterpillar",
            model="320",
            hours=6200.0,
            location="Dubai",
            description=None,
        )


def test_listing_valid_listing():
    listing = Listing(
        listing_id="1001",
        title="Caterpillar 320 Excavator",
        price_usd=85000.0,
        year=2018,
        brand="Caterpillar",
        model="320",
        hours=6200.0,
        location="Dubai",
        description=None,
    )

    assert listing.brand == "Caterpillar"


def test_listing_nan_to_none():
    listing = Listing(
        listing_id="1002",
        title="Komatsu D65 Bulldozer",
        price_usd=float("nan"),
        year=2015,
        brand="Komatsu",
        model="D65",
        hours=float("nan"),
        location="Abu Dhabi",
        description=None,
    )

    assert listing.price_usd is None
    assert listing.hours is None


def test_real_row_validates_from_data_file():
    # Load DATA_FILE with load_listings and take it into records, build a listing from each row, and assert there are 11
    from heavy_equipment_search.loader import load_listings

    DATA_FILE = "data/listings.csv"
    df = load_listings(DATA_FILE)
    records = df.to_dict(orient="records")
    listings = [Listing(**row) for row in records]
    assert len(listings) == 11
