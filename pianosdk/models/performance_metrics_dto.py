from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class PerformanceMetricsDto(BaseModel):
    ga_account: Optional[str]
    is_enabled: Optional[str]
    track_only_aids: Optional[str]


PerformanceMetricsDto.update_forward_refs()
