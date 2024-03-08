import os
import uvicorn

from . import app


PORT = int(os.environ.get("PORT", 8000))


uvicorn.run(
    app,
    host="0.0.0.0",
    port=PORT,
    log_config=None,
)
