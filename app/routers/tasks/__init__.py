from fastapi import APIRouter

from .controller import handle_get, handle_post
from .validation import RequestBodyPost, ResponseBodyPost, ResponseBodyGet


router = APIRouter(prefix='/task')


@router.post('')
async def create_task(body: RequestBodyPost) -> ResponseBodyPost:
    return await handle_post(body)


@router.get('')
async def fatch_all_tasks() -> ResponseBodyGet:
    return await handle_get()
