FROM python:3.11-slim-buster

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install transformers
RUN pip install torch
RUN pip install accelerate

CMD ["python", "app.py"]