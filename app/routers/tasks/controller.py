from fastapi import Request
from fastapi.responses import JSONResponse

from .validation import Task, ResponseBodyPost, ResponseBodyGet


async def handle_post(body: Task) -> ResponseBodyPost:
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
        })


async def handle_get(request: Request) -> ResponseBodyGet:
    async with request.app.state.conn_pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('SELECT * FROM tasks;')
            data = [row async for row in cur]

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "data": data
        })
