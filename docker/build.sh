#!/usr/bin/env bash

cp ../requirements.txt requirements.txt

TAG="service/flask/template"
VERSION=0.0.1

tag="$TAG:$VERSION"

echo "Executing docker build with tag: $tag"
docker build -t ${tag} .

rm requirements.txt