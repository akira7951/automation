from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.id.models.custom_field_attribute_dto import CustomFieldAttributeDto
from pianosdk.id.models.tooltip import Tooltip
from pianosdk.id.models.validator import Validator
from typing import List


class CustomFieldDefinitionDto(BaseModel):
    field_name: Optional[str]
    title: Optional[str]
    comment: Optional[str]
    editable: Optional[bool]
    data_type: Optional[str]
    validators: Optional['List[Validator]']
    options: Optional[List[str]]
    favourite_options: Optional[List[str]]
    options_link: Optional[int]
    set_name: Optional[str]
    required_by_default: Optional[bool]
    values_count: Optional[int]
    archived: Optional[bool]
    default_sort_order: Optional[int]
    attribute: Optional['CustomFieldAttributeDto']
    tooltip: Optional['Tooltip']
    parent: Optional[int]
    hidden: Optional[bool]


CustomFieldDefinitionDto.update_forward_refs()
