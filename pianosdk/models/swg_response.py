from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class SwgResponse(BaseModel):
    subscription_token: Optional[str]
    detail: Optional[str]
    products: Optional[List[str]]


SwgResponse.update_forward_refs()
