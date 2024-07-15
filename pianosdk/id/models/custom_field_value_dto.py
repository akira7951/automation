from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CustomFieldValueDto(BaseModel):
    field_name: Optional[str]
    value: Optional[str]
    created: Optional[datetime]
    email_creator: Optional[str]
    sort_order: Optional[int]


CustomFieldValueDto.update_forward_refs()
