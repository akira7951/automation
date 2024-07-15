from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class ClientConfigurationsDto(BaseModel):
    ga_account: Optional[str]
    is_performance_metrics_enabled: Optional[str]
    performance_metrics_ga_account: Optional[str]
    performance_metrics_track_only_aids: Optional[str]
    msqa_client_id: Optional[str]


ClientConfigurationsDto.update_forward_refs()
