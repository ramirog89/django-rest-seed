FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV SETTINGS="src.app.config.settings.development"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./ /app

RUN chmod -R 777 /app
RUN pip3 install packaging

RUN adduser -D user
USER user

CMD exec python manage.py runserver 0.0.0.0:7000 --settings=$SETTINGS