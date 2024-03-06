import os
import uvicorn

from . import app


PORT = int(os.environ.get("PORT", 8000))
LOG_LEVEL = int(os.environ.get("LOG_LEVEL", 20))


uvicorn.run(
    app,
    host="0.0.0.0",
    port=PORT,
    log_level=LOG_LEVEL
)
