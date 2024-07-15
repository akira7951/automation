from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class OAuthRequest(BaseModel):
    client_id: Optional[str]
    refresh_token: Optional[str]
    grant_type: Optional[str]
    code: Optional[str]
    client_secret: Optional[str]
    redirect_uri: Optional[str]
    code_verifier: Optional[str]


OAuthRequest.update_forward_refs()
