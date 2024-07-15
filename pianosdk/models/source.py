from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class Source(BaseModel):
    type: Optional[str]
    source_names: Optional[List[str]]


Source.update_forward_refs()
