from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class AccessTokenList(BaseModel):
    value: Optional[str]
    cookie_domain: Optional[str]


AccessTokenList.update_forward_refs()
