FROM python:3.12.0a6-slim-buster

WORKDIR /app

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linus-headers
RUN apk add --no-cache jpeg-dev zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]