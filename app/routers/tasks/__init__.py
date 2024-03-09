from fastapi import APIRouter, Request

from .controller import handle_get, handle_post
from .validation import RequestBody, ResponseBodyPost, ResponseBodyGet


router = APIRouter(prefix="/task")


@router.post("")
async def create_task(body: RequestBody, request: Request) -> ResponseBodyPost:
    return await handle_post(body, request)


@router.get("")
async def fatch_all_tasks(request: Request) -> ResponseBodyGet:
    return await handle_get(request)
