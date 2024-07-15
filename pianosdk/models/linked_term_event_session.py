from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.linked_term_event_page_view_content import LinkedTermEventPageViewContent
from pianosdk.anon.models.linked_term_event_session_offer import LinkedTermEventSessionOffer


class LinkedTermEventSession(BaseModel):
    tracking_id: Optional[str]
    tbc: Optional[str]
    pcid: Optional[str]
    offer: Optional['LinkedTermEventSessionOffer']
    page_view_id: Optional[str]
    page_view_content: Optional['LinkedTermEventPageViewContent']
    user_agent: Optional[str]
    consents: Optional[str]
    previous_user_segments: Optional[str]


LinkedTermEventSession.update_forward_refs()
