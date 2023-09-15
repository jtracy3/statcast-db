FROM python:3.10-slim

RUN mkdir /app

COPY app /app

WORKDIR /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "python", "main.py" ]
#ENTRYPOINT ["/bin/sh"]