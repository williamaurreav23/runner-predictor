FROM python:3.7-alpine
LABEL maintainer="m.mojek@gmail.com"

ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /requirements.txt 
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /django_code
WORKDIR /django_code

COPY . /django_code/

RUN adduser -D user
USER user

#EXPOSE 8000
#STOPSIGNAL SIGINT