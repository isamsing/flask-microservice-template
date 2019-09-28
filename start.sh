#!/usr/bin/env bash

service nginx start
uwsgi /service/conf/uwsgi.ini --thunder-lock --cache2 name=cache,maxitems=10,bitmap=1 >> /service/log/uwsgi.log 2>&1