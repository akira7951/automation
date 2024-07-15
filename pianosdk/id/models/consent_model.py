from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ConsentModel(BaseModel):
    consent_pub_id: Optional[str]
    display_text: Optional[str]
    field_name: Optional[str]
    field_id: Optional[str]
    sort_order: Optional[int]
    checked: Optional[bool]
    required: Optional[bool]


ConsentModel.update_forward_refs()
