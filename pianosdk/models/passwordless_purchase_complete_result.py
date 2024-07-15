from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.resource import Resource
from typing import List


class PasswordlessPurchaseCompleteResult(BaseModel):
    oid: Optional[str]
    url: Optional[str]
    resource: Optional['Resource']
    show_offer_params: Optional[str]
    type: Optional[str]
    process_id: Optional[str]
    polling_enabled: Optional[bool]
    polling_timeouts: Optional[List[int]]


PasswordlessPurchaseCompleteResult.update_forward_refs()
