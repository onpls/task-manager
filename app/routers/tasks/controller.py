from fastapi.responses import JSONResponse

from .validation import Task, ResponseBodyPost, ResponseBodyGet


async def handle_post(body: Task) -> ResponseBodyPost:
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
        })


async def handle_get() -> ResponseBodyGet:
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "data": []
        })
