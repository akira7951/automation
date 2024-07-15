from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import Any
from typing import Dict
from typing import List


class Validator(BaseModel):
    type: Optional[str]
    params: Optional['Dict[str, Any]']
    error_message: Optional[str]


Validator.update_forward_refs()
