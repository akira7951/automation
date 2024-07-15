from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ResourceDto(BaseModel):
    rid: Optional[str]
    aid: Optional[str]
    name: Optional[str]
    description: Optional[str]
    image_url: Optional[str]


ResourceDto.update_forward_refs()
