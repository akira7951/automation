from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublisherSetPasswordRequest(BaseModel):
    aid: Optional[str]
    reset_password_token: Optional[str]
    password: Optional[str]


PublisherSetPasswordRequest.update_forward_refs()
