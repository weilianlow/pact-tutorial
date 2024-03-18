# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /pact-tutorial

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "app/views", "run", "--host=0.0.0.0"]