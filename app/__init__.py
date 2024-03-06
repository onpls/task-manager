import os

from fastapi import FastAPI

from . import routers

PORT = int(os.environ.get("PORT", 8000))
LOG_LEVEL = int(os.environ.get("PORT", 20))

app = FastAPI()

app.include_router(routers.root)
