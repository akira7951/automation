from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublisherRegisterRequest(BaseModel):
    aid: Optional[str]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    password: Optional[str]
    consents: Optional[str]
    custom_fields: Optional[str]
    form_id: Optional[str]
    passwordless: Optional[bool]
    magic_link_sent: Optional[bool]


PublisherRegisterRequest.update_forward_refs()
