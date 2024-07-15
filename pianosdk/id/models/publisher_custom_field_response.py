from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublisherCustomFieldResponse(BaseModel):
    name: Optional[str]
    value: Optional[str]


PublisherCustomFieldResponse.update_forward_refs()
