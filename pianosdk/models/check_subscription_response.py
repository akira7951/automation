from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class CheckSubscriptionResponse(BaseModel):
    type: Optional[str]
    user_token: Optional[str]
    term_id: Optional[str]


CheckSubscriptionResponse.update_forward_refs()
