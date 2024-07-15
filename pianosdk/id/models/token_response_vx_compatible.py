from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.id.models.data import Data


class TokenResponseVxCompatible(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]
    refresh_token: Optional[str]
    code: Optional[int]
    expires_in: Optional[int]
    ts: Optional[int]
    data: Optional['Data']


TokenResponseVxCompatible.update_forward_refs()
