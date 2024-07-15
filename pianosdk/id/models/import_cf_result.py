from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Dict
from typing import List


class ImportCFResult(BaseModel):
    code: Optional[int]
    ts: Optional[int]
    data: Optional['Dict[str, List[Dict[str, str]]]']


ImportCFResult.update_forward_refs()
