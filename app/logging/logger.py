import json
import logging
import os

from datetime import datetime

LOG_LEVEL = int(os.environ.get("LOG_LEVEL", logging.INFO))


class JsonFormatter(logging.Formatter):
    def format(self, record):
        if record.exc_info:
            # This can be solved better with json traceback formtter
            return super().formatException(record.exc_info)
        else:
            json_record = {
                "level": logging.getLevelName(record.levelno),
                "message": record.getMessage(),
                "timestamp": datetime.now().isoformat(),
            }
            if "request" in record.__dict__:
                json_record["request"] = record.__dict__["request"]
            if "response" in record.__dict__:
                json_record["response"] = record.__dict__["response"]
            if "json_fields" in record.__dict__:
                json_record = {**json_record, **record.__dict__["json_fields"]}
            return json.dumps(json_record, indent=2, default=str)


logger = logging.root
logger.setLevel(LOG_LEVEL)

for handler in [logging.StreamHandler()]:
    handler.setFormatter(JsonFormatter())
    logger.addHandler(handler)

logging.getLogger("uvicorn.access").disabled = True
