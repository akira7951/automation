from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class BillingPlanTranslationRequest(BaseModel):
    billing_plan: Optional[str]
    subscription_last_payment: Optional[datetime]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    term_pub_id: Optional[str]


BillingPlanTranslationRequest.update_forward_refs()
