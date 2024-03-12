FROM python:3.8-slim

WORKDIR /app

COPY . /app
COPY data.json /app/data.json

ENV TZ=Europe/Athens

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
