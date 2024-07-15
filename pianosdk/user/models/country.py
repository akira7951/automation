from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Country(BaseModel):
    country_name: Optional[str]
    country_code: Optional[str]
    country_id: Optional[str]


Country.update_forward_refs()
