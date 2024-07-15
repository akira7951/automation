from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.resource import Resource


class Term(BaseModel):
    term_id: Optional[str]
    aid: Optional[str]
    resource: Optional['Resource']
    type: Optional[str]
    name: Optional[str]
    description: Optional[str]
    create_date: Optional[datetime]


Term.update_forward_refs()
