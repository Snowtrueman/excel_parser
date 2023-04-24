FROM python:3.10.10-alpine

WORKDIR /usr/src/app

RUN mkdir /usr/src/app/static

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .