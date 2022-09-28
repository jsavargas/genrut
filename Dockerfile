FROM python:3.10.2-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY rutchile.py .

RUN chmod +x /app/rutchile.py

CMD ["python3", "./rutchile.py"]
