from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkedTermCheckoutTrackParams(BaseModel):
    aid: Optional[str]
    browser_id: Optional[str]
    external_term_id: Optional[str]
    checkout_start_date: Optional[int]


LinkedTermCheckoutTrackParams.update_forward_refs()
