from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.id.models.publisher_custom_field_response import PublisherCustomFieldResponse
from typing import List


class PublisherUserProfileResponse(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    uid: Optional[str]
    email: Optional[str]
    create_date: Optional[int]
    reset_password_email_sent: Optional[bool]
    password: Optional[str]
    custom_fields: Optional['List[PublisherCustomFieldResponse]']


PublisherUserProfileResponse.update_forward_refs()
