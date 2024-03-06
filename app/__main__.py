import uvicorn

from .import app, PORT, LOG_LEVEL


uvicorn.run(
    app,
    host="0.0.0.0",
    port=PORT,
    log_level=LOG_LEVEL
)
