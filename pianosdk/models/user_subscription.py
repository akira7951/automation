from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.term import Term


class UserSubscription(BaseModel):
    subscription_id: Optional[str]
    term: Optional['Term']
    auto_renew: Optional[bool]
    grace_period_start_date: Optional[datetime]
    next_bill_date: Optional[datetime]
    start_date: Optional[datetime]
    status: Optional[str]
    cancelable: Optional[bool]
    cancelable_and_refundadle: Optional[bool]
    payment_billing_plan_description: Optional[str]


UserSubscription.update_forward_refs()
