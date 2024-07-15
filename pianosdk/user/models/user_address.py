from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.user.models.country import Country
from pianosdk.user.models.region import Region


class UserAddress(BaseModel):
    user_address_id: Optional[str]
    region: Optional['Region']
    country: Optional['Country']
    city: Optional[str]
    postal_code: Optional[str]
    company_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    personal_name: Optional[str]
    address1: Optional[str]
    address2: Optional[str]
    phone: Optional[str]


UserAddress.update_forward_refs()
