from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.id.models.consent_model import ConsentModel
from pianosdk.id.models.custom_field_value_dto import CustomFieldValueDto
from typing import List


class SocialAdditionalInputRequest(BaseModel):
    additional_input_state: Optional[str]
    consents: Optional['List[ConsentModel]']
    custom_field_values: Optional['List[CustomFieldValueDto]']
    email: Optional[str]


SocialAdditionalInputRequest.update_forward_refs()
