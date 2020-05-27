FROM python:3.6.10-alpine3.11

WORKDIR /src

COPY . /src

RUN apk add --update gcc musl-dev graphviz-dev && \
    pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ['python', 'manage.py', 'runserver', '0.0.0.0:8000']