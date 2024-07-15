from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Resource(BaseModel):
    rid: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    description: Optional[str]
    image_url: Optional[str]


Resource.update_forward_refs()
