from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.access import Access
from pianosdk.anon.models.term import Term


class TermConversion(BaseModel):
    term_conversion_id: Optional[str]
    term: Optional['Term']
    type: Optional[str]
    aid: Optional[str]
    user_access: Optional['Access']
    create_date: Optional[datetime]


TermConversion.update_forward_refs()
