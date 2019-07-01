FROM ubuntu:16.04

MAINTAINER Samneet Singh <samneets@blueplanet.com>

ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5000
ENV TERM=xterm

WORKDIR /service

RUN apt-get update
RUN apt-get install apt-utils mariadb-client --assume-yes
RUN apt-get install gcc unzip --assume-yes
RUN wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
RUN bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p ~/anaconda
RUN rm Anaconda3-4.2.0-Linux-x86_64.sh
RUN echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc
RUN source ~/.bashrc && conda update conda

RUN conda install python=3.6.8
RUN conda install gcc
RUN conda install libgcc

ADD requirements.txt /service
RUN pip install -r /service/requirements.txt

ADD ../app /service/

CMD python /service/app/app.py >> /service/log/service.log 2>&1


