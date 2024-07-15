from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PaymentMethod(BaseModel):
    upi_nickname: Optional[str]
    upi_color: Optional[str]
    upi_number: Optional[str]
    upi_expiration_month: Optional[int]
    upi_expiration_year: Optional[int]
    upi_postal_code: Optional[str]
    description: Optional[str]
    user_payment_info_id: Optional[str]


PaymentMethod.update_forward_refs()
