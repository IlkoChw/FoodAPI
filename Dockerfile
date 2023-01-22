FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN set -x \
    && apt-get update \
    && apt-get -y install sudo \
    && apt-get -y update \
    && sudo apt-get update -y \
    && sudo apt install gettext -y \
    && pip install --upgrade pip

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app
