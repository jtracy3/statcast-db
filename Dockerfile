FROM python:3.10-slim

RUN mkdir /app

COPY app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT [ "python", "app/test1.py" ]
#ENTRYPOINT ["/bin/sh"]