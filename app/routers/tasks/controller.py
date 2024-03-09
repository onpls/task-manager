from fastapi import Request
from fastapi.responses import JSONResponse

from .validation import Task, ResponseBodyPost, ResponseBodyGet


async def handle_post(task: Task, request: Request) -> ResponseBodyPost:
    async with request.app.state.conn_pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await task.save(cursor, table="tasks", pk="id")

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
        })


async def handle_get(request: Request) -> ResponseBodyGet:
    async with request.app.state.conn_pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT * FROM tasks;")
            tasks = await Task.from_cursor(cursor)

    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "data": [task.model_dump() for task in tasks]
        })
