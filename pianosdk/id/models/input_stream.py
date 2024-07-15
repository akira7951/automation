from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional


class InputStream(BaseModel):
    pass


InputStream.update_forward_refs()
