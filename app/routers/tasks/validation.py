from pydantic import BaseModel


class Task(BaseModel):
    info: str


class RequestBodyPost(Task):
    pass


class ResponseBodyPost(BaseModel):
    success: bool


class ResponseBodyGet(ResponseBodyPost):
    data: list[Task]
