from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Tooltip(BaseModel):
    enabled: Optional[bool]
    type: Optional[str]
    text: Optional[str]


Tooltip.update_forward_refs()
