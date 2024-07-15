from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.user.models.resource_dto import ResourceDto
from pianosdk.user.models.user_dto import UserDto


class AccessDTO(BaseModel):
    access_id: Optional[str]
    parent_access_id: Optional[str]
    granted: Optional[bool]
    user: Optional['UserDto']
    resource: Optional['ResourceDto']
    expire_date: Optional[datetime]
    start_date: Optional[datetime]
    can_revoke_access: Optional[bool]
    custom_data: Optional[str]


AccessDTO.update_forward_refs()
