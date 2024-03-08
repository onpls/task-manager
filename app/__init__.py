from fastapi import FastAPI

from . import routers
from . import connections
from . import logging

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    await connections.establish(app)


@app.on_event("shutdown")
async def shutdown_event():
    await connections.close(app)

app.add_middleware(logging.LogMiddleware)
logging.add_exc_handler(app)

app.include_router(routers.root)
