from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PublicCaptchaConfig(BaseModel):
    aid: Optional[str]
    enabled: Optional[bool]
    captcha3_site_key: Optional[str]


PublicCaptchaConfig.update_forward_refs()
