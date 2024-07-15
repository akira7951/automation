from datetime import date, datetime
from pydantic.main import BaseModel
from typing import Optional
from typing import List


class LinkedTermEventPageViewContent(BaseModel):
    content_created: Optional[str]
    content_author: Optional[str]
    content_section: Optional[str]
    content_type: Optional[str]
    tags: Optional[List[str]]


LinkedTermEventPageViewContent.update_forward_refs()
