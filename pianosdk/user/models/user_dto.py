from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class UserDto(BaseModel):
    uid: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    email: Optional[str]
    image1: Optional[str]


UserDto.update_forward_refs()
