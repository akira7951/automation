from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class LocaleModel(BaseModel):
    locale: Optional[str]
    label: Optional[str]
    localized_label: Optional[str]
    is_default: Optional[bool]
    is_enabled: Optional[bool]
    is_rtl: Optional[bool]


LocaleModel.update_forward_refs()
