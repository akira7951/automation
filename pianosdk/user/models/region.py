from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Region(BaseModel):
    region_name: Optional[str]
    region_code: Optional[str]
    region_id: Optional[str]


Region.update_forward_refs()
