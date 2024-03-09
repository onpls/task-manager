FROM python:3.11.6-slim

WORKDIR /usr/src

COPY pyproject.toml poetry.lock /usr/src
RUN pip install poetry
RUN poetry install

COPY app/ ./app/

CMD poetry run python -m app
