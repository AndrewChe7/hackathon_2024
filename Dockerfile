FROM python:latest

COPY requirements.txt /temp/requirements.txt
COPY back /back

WORKDIR /back

EXPOSE 8000


# RUN apk add posgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt