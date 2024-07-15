from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LinkedTermEventSessionOffer(BaseModel):
    offer_id: Optional[str]
    offer_template_id: Optional[str]
    offer_template_version_id: Optional[str]


LinkedTermEventSessionOffer.update_forward_refs()
