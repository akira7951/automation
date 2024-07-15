from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.id.models.social_linking_response import SocialLinkingResponse


class TokenResponse(BaseModel):
    access_token: Optional[str]
    token_type: Optional[str]
    refresh_token: Optional[str]
    code: Optional[str]
    error: Optional[str]
    error_description: Optional[str]
    expires_in: Optional[int]
    preauth_token: Optional[str]
    social_linking_response: Optional['SocialLinkingResponse']
    registration: Optional[bool]
    site_cookie_domain: Optional[str]
    email_confirmation_required: Optional[bool]
    login_token_id: Optional[str]
    extend_expired_access_enabled: Optional[bool]
    direction_url: Optional[str]
    passwordless_token: Optional[str]
    pub_id: Optional[str]
    authorized_by_sso: Optional[bool]
    message: Optional[str]
    sso_confirmation: Optional[bool]
    two_factor_auth_required: Optional[bool]


TokenResponse.update_forward_refs()
