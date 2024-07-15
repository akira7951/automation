from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserModel(BaseModel):
    uid: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    valid: Optional[bool]


UserModel.update_forward_refs()
