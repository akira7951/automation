from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from pianosdk.anon.models.external_css import ExternalCss
from typing import List


class LightOfferTemplateVersion(BaseModel):
    offer_template_id: Optional[str]
    token_type: Optional[str]
    version: Optional[int]
    type: Optional[str]
    content1_type: Optional[str]
    content2_type: Optional[str]
    content1_value: Optional[str]
    content2_value: Optional[str]
    template_id: Optional[str]
    template_version_id: Optional[str]
    is_offer_template_archived: Optional[bool]
    is_template_variant_archived: Optional[bool]
    external_css_list: Optional['List[ExternalCss]']


LightOfferTemplateVersion.update_forward_refs()
