from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.resource import Resource


class PasswordlessPurchaseCheckResult(BaseModel):
    poll_status: Optional[str]
    resource: Optional['Resource']
    show_offer_params: Optional[str]
    type: Optional[str]


PasswordlessPurchaseCheckResult.update_forward_refs()
