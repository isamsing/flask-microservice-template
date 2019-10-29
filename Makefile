NAME=service/flask/template
VERSION=0.0.1
TAG = $(NAME):$(VERSION)

help:
	@echo "help: To get all the commands"
	@echo "push: To push the docker image"
	@echo "build: To build the docker image"
	@echo "run: To start a new docker container";

push:
	@echo "pushing docker image tag: $(TAG)"
	docker push $(TAG);

tag:
	@echo "Tagging docker image tag: $(TAG)"
	docker tag $(TAG) $(NAME):latest;

build:
	@echo "Building docker image tag: $(TAG)"
	zip app.zip -q -r app -i "*.py"
	@docker build -t $(NAME):latest .
	rm app.zip;

run:
	@echo "Running docker image tag: $(TAG)"
	docker run -d -p 5000:5000 --name test $(TAG);

