FROM continuumio/anaconda3

MAINTAINER Samneet Singh <samneetdhillon@hotmail.com>

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
ENV PATH /opt/conda/bin/:$PATH

WORKDIR /service

RUN apt-get update
RUN apt-get install apt-utils mariadb-client --assume-yes
RUN apt-get install gcc unzip --assume-yes

ADD requirements.txt /service
RUN conda remove lxml
RUN conda install -c conda-forge lxml
RUN conda install -c conda-forge libiconv
RUN pip install -r /service/requirements.txt
RUN conda install -c conda-forge uwsgi

RUN mkdir /service/conf
ADD uwsgi.ini /service/conf/

ADD app.zip /service/
RUN unzip /service/app.zip
RUN mkdir -p /service/log

CMD uwsgi /service/conf/uwsgi.ini --thunder-lock --cache2 name=cache,maxitems=10,bitmap=1 >> /service/log/uwsgi.log 2>&1