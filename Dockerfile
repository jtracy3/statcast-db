FROM python:3.10.7-alpine

RUN apt-get update -y
RUN apt-get install vim

RUN mkdir /app

COPY app /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "/app/main.py" ]
