from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublicRestorePasswordRequest(BaseModel):
    reset_password_token: Optional[str]
    password: Optional[str]


PublicRestorePasswordRequest.update_forward_refs()
