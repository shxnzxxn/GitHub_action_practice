FROM python:3.8-slim-buster

COPY . /app
WORKDIR /app

RUN pip install pytest

CMD python3 practice.py