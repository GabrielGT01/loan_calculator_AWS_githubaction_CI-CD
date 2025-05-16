
FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN apt update -y && apt install -y awscli

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 5001

CMD ["python3", "app.py"]
