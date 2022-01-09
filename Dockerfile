FROM python:3.8.5-alpine

COPY . /app
WORKDIR /app

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev  mariadb-dev build-base gcc libc-dev libffi-dev && apk add py3-pip &&  pip install --upgrade pip && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd


RUN pip install -r requirements1.txt