FROM ubuntu:16.04

MAINTAINER Samneet Singh <samneetdhillon@hotmail.com>

ENV BASH_ENV=".bashrc"
ENV TERM=xterm
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000

WORKDIR /service

RUN apt-get update
RUN apt-get install apt-utils mariadb-client --assume-yes
RUN apt-get install gcc unzip --assume-yes
RUN apt install -y wget
RUN apt-get install -y bzip2
RUN wget https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh
RUN bash Anaconda3-5.0.1-Linux-x86_64.sh -b -p ~/anaconda
RUN rm Anaconda3-5.0.1-Linux-x86_64.sh
RUN echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc
RUN source ~/.bashrc && conda update conda

RUN conda install python=3.6.8
RUN conda install gcc
RUN conda install libgcc

ADD requirements.txt /service
RUN pip install -r /service/requirements.txt

ADD ../app /service/

CMD python /service/app/run.py >> /service/log/service.log 2>&1


