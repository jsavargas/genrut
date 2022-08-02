FROM python:3.10.2-alpine

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY rutchile.py .

