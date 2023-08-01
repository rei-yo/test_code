FROM python:3
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir app

COPY ./django_pj /app
#作業ディレクトリ
WORKDIR /app 

# CMD ["python3", "manage.py", "runserver"]

# 以下チュートリアルより
# FROM python:3

# 以下は何を環境変数に設定している？
# ENV PYTHONUNBUFFERED 1　  
# RUN mkdir /code
# WORKDIR /code
# ADD requirements.txt /code/
# RUN pip install -r requirements.txt
# ADD . /code/
