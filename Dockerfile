FROM python:3.8-slim

WORKDIR /app

COPY src/ /app
COPY requirements.txt /app/requirements.txt
COPY main.py /app/main.py

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
