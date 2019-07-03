FROM continuumio/anaconda3

MAINTAINER Samneet Singh <samneetdhillon@hotmail.com>

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

WORKDIR /service

RUN apt-get update
RUN apt-get install apt-utils mariadb-client --assume-yes
RUN apt-get install gcc unzip --assume-yes

ADD requirements.txt /service
RUN pip install -r /service/requirements.txt

ADD app.zip /service/
RUN unzip /service/app.zip
RUN mkdir -p /service/log

#CMD python /service/app/run.py >> /service/log/service.log 2>&1


