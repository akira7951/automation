from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ExternalCss(BaseModel):
    title: Optional[str]
    url: Optional[str]
    status: Optional[str]
    position: Optional[int]
    external_css_id: Optional[str]


ExternalCss.update_forward_refs()
