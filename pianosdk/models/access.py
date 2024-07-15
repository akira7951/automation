from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.resource import Resource
from pianosdk.anon.models.user import User


class Access(BaseModel):
    access_id: Optional[str]
    parent_access_id: Optional[str]
    granted: Optional[bool]
    user: Optional['User']
    resource: Optional['Resource']
    expire_date: Optional[datetime]
    start_date: Optional[datetime]
    can_revoke_access: Optional[bool]


Access.update_forward_refs()
