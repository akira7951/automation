from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.user_model import UserModel


class UserInfo(BaseModel):
    user_lang: Optional[str]
    is_new_customer: Optional[bool]
    user: Optional['UserModel']
    country_code: Optional[str]
    postal_code: Optional[str]
    tax_support: Optional[str]


UserInfo.update_forward_refs()
