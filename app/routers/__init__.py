from fastapi import APIRouter

from . import tasks

root = APIRouter()

root.include_router(tasks.router)
