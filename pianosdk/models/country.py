from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.region import Region
from typing import List


class Country(BaseModel):
    country_name: Optional[str]
    country_code: Optional[str]
    country_id: Optional[str]
    regions: Optional['List[Region]']


Country.update_forward_refs()
