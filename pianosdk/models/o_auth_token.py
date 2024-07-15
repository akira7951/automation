from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class OAuthToken(BaseModel):
    access_token: Optional[str]
    expires_in: Optional[int]
    refresh_token: Optional[str]
    token_type: Optional[str]


OAuthToken.update_forward_refs()
