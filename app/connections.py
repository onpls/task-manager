import aiopg
import os
import logging

from fastapi import FastAPI


DB_URI = os.environ.get("DB_URI", None)


async def establish(app: FastAPI):
    try:
        app.state.conn_pool = await aiopg.create_pool(DB_URI)
        logging.info("Postgres connection available")
    except Exception as exception:
        logging.info("Unable to init database client")
        raise exception


async def close(app: FastAPI):
    await app.state.conn_pool.close()
