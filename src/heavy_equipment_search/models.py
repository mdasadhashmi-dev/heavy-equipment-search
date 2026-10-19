import math

from pydantic import BaseModel, field_validator


class Listing(BaseModel):
    listing_id: str
    title: str
    price_usd: float | None
    year: int | None
    brand: str | None
    model: str | None
    hours: float | None
    location: str
    description: str | None

    @field_validator("price_usd", "hours", mode="before")
    @classmethod
    def nan_to_none(cls, value):
        if isinstance(value, float) and math.isnan(value):
            return None
        return value
