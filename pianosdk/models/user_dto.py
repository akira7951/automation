from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserDto(BaseModel):
    uid: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    create_date: Optional[datetime]


UserDto.update_forward_refs()
