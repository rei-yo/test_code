FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir app
WORKDIR /app 
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./django_pj /app/

CMD ["/startup.sh"]

#作業ディレクトリ

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
