from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.user_info import UserInfo


class TemplateContext(BaseModel):
    user_info: Optional['UserInfo']
    experience_id: Optional[str]
    experience_action_id: Optional[str]
    experience_execution_id: Optional[str]
    template_language: Optional[str]


TemplateContext.update_forward_refs()
