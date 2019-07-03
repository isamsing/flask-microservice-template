#!/usr/bin/env bash

cd ../
zip app.zip -q -r app -i "*.py"
mv -f app.zip docker/
cd docker

cp ../requirements.txt requirements.txt

TAG="service/flask/template"
VERSION=0.0.1

tag="$TAG:$VERSION"

echo "Executing docker build with tag: $tag"
docker build -t ${tag} .

rm requirements.txt
rm app.zip