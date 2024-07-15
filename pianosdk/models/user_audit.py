from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserAudit(BaseModel):
    uid: Optional[str]
    action_type: Optional[str]
    aid: Optional[str]


UserAudit.update_forward_refs()
