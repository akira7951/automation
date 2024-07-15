from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class MobileLoginRequest(BaseModel):
    client_id: Optional[str]
    code: Optional[str]
    code_verifier: Optional[str]
    provider_access_token: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    social_type: Optional[str]


MobileLoginRequest.update_forward_refs()
