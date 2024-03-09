from aiopg import Cursor
from pydantic import BaseModel
from typing import Optional


class BaseDataModel(BaseModel):

    @classmethod
    async def from_cursor(cls, cursor: Cursor, limit: int = None) -> list:
        rows = await cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        dict_results = [dict(zip(columns, row)) for row in rows]
        model_objects = [cls(**item) for item in dict_results]
        return model_objects


class Task(BaseDataModel):
    id: Optional[int]
    name: str
    completion_status: bool


class RequestBodyPost(Task):
    pass


class ResponseBodyPost(BaseModel):
    success: bool


class ResponseBodyGet(ResponseBodyPost):
    data: list[Task]
