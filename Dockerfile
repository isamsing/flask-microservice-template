FROM continuumio/anaconda3

MAINTAINER Samneet Singh <samneetdhillon@hotmail.com>

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
ENV PATH /opt/conda/bin/:$PATH

WORKDIR /service

RUN apt-get update
RUN apt-get install nginx --assume-yes
RUN apt-get install apt-utils mariadb-client --assume-yes
RUN apt-get install gcc unzip --assume-yes

ADD requirements.txt /service
RUN conda remove lxml
RUN conda install -c conda-forge lxml
RUN conda install -c conda-forge libiconv
RUN pip install -r /service/requirements.txt
RUN conda install -c conda-forge uwsgi

RUN mkdir /service/conf
COPY uwsgi.ini /service/conf/
COPY nginx.conf /etc/nginx/
COPY start.sh /service/

ADD app.zip /service/
RUN unzip /service/app.zip
RUN mkdir -p /service/log
RUN rm /service/app.zip

CMD ./start.sh

