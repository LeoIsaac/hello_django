FROM python:3.5.2-alpine

RUN apk update && \
    apk add --no-cache gcc postgresql-dev musl-dev postgresql-client

ADD requirements.txt /
RUN pip install -r requirements.txt
