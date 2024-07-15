from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class Currency(BaseModel):
    currency_code: Optional[str]
    currency_symbol: Optional[str]


Currency.update_forward_refs()
