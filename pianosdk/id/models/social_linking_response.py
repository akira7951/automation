from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class SocialLinkingResponse(BaseModel):
    identity_social_linking_state: Optional[str]
    password_confirmation_available: Optional[bool]
    linked_social_accounts: Optional[List[str]]
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    social_type: Optional[str]
    is_passwordless: Optional[bool]


SocialLinkingResponse.update_forward_refs()
