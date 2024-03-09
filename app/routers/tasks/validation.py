from pydantic import BaseModel
from typing import Optional

from ...models import BaseDataModel


class Task(BaseDataModel):
    id: Optional[int] = None
    name: str
    completion_status: Optional[bool] = False


class RequestBodyPost(Task):
    pass


class ResponseBodyPost(BaseModel):
    success: bool


class ResponseBodyGet(ResponseBodyPost):
    data: list[Task]
