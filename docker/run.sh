#!/usr/bin/env bash

TAG="service/flask/template"
VERSION=0.0.1

tag="$TAG:$VERSION"

docker run \
    -d \
    -p 5000:5000 \
    --name test ${tag}