FROM python:3.11.6-slim

WORKDIR /usr/src

ARG DB_URI
ENV DB_URI="${DB_URI}"

COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install

COPY alembic/ ./alembic/
COPY alembic.ini ./alembic.ini

COPY app/ ./app/
CMD poetry run alembic upgrade head && poetry run python -m app
