from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class GeoLocation(BaseModel):
    region_code: Optional[str]
    region_name: Optional[str]
    city: Optional[str]
    country_code: Optional[str]
    postal_code: Optional[str]


GeoLocation.update_forward_refs()
