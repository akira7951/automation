from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.linked_term_page_view_content_params import LinkedTermPageViewContentParams


class LinkedTermSessionParams(BaseModel):
    tracking_id: Optional[str]
    tbc: Optional[str]
    pcid: Optional[str]
    offer_id: Optional[str]
    offer_template_id: Optional[str]
    offer_template_version_id: Optional[str]
    page_view_id: Optional[str]
    page_view_content: Optional['LinkedTermPageViewContentParams']
    consents: Optional[str]
    previous_user_segments: Optional[str]


LinkedTermSessionParams.update_forward_refs()
