From ubuntu:20.04
USER root

RUN apt update
RUN apt install -y python3.9
RUN apt install -y python3-pip
COPY requirements.txt .
RUN python3.9 -m pip install -r requirements.txt

RUN mkdir app

COPY ./django_pj /app
#作業ディレクトリ
WORKDIR /app 

CMD ["python3", "manage.py", "runserver"]

# 以下チュートリアルより
# FROM python:3

# 以下は何を環境変数に設定している？
# ENV PYTHONUNBUFFERED 1　  
# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/
