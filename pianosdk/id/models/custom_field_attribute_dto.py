from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class CustomFieldAttributeDto(BaseModel):
    date_format: Optional[str]
    autofill: Optional[bool]
    default: Optional[bool]
    dmp_segmentation_enable: Optional[bool]
    multiline: Optional[bool]
    default_value: Optional[str]
    placeholder: Optional[str]
    pre_select_country_by_ip: Optional[bool]
    _global: Optional[bool]
    global_status: Optional[str]
    aid_list: Optional[List[str]]
    linked_term_field: Optional[bool]


CustomFieldAttributeDto.update_forward_refs()
