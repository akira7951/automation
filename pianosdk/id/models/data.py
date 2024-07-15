from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Data(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]
    refresh_token: Optional[str]
    expires_in: Optional[int]


Data.update_forward_refs()
