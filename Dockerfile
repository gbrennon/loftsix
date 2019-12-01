FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY . /code/

WORKDIR /code/

RUN flask migrations