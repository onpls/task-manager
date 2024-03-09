from fastapi import HTTPException


class ExpectedError(HTTPException):
    def __init__(self, data: str):
        super().__init__(
            status_code=400,
            detail={
                "message": "Sample message",
                "additionalData": data
            }
        )
