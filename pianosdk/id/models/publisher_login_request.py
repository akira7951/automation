from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublisherLoginRequest(BaseModel):
    aid: Optional[str]
    email: Optional[str]
    password: Optional[str]
    stay_logged_in: Optional[bool]


PublisherLoginRequest.update_forward_refs()
