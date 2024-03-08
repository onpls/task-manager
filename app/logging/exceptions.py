from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .logger import logger


def add_exc_handler(app: FastAPI):
    @app.exception_handler(Exception)
    @app.exception_handler(HTTPException)
    async def exception_handler(request: Request, exc: Exception):
        if isinstance(exc, HTTPException) and exc.status_code < 500:
            status = exc.status_code
            response_detail = exc.detail
            logger.error(
                f"Service failed with status {status}",
                extra={
                    "json_fields": {
                        "detail": exc.detail
                    }})
        else:
            status = 500
            response_detail = "Internal Server Error"

        return JSONResponse(
            status_code=status,
            content=jsonable_encoder(
                {"success": False, "detail": response_detail}
            ))
