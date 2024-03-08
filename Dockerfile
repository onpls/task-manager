FROM python:3.11.6-slim

WORKDIR /usr/src

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

CMD python -m app
