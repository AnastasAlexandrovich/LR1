FROM python:3.9.5-alpine3.12

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN apk update \
    && apk add alpine-sdk gcc musl-dev python3-dev libffi-dev openssl-dev cargo jpeg-dev zlib-dev  ffmpeg

RUN pip install --upgrade pip
RUN apk add postgresql-dev gcc python3-dev musl-dev
COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . /usr/src/app/

