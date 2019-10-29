NAME=service/flask/template
VERSION=0.0.1

help:
	@echo "help: To get all the commands"
	@echo "push: To push the docker image"
	@echo "build: To build the docker image"
	@echo "run: To start a new docker container";

push:
	@echo "pushing docker image tag: $(NAME):$(VERSION)"
	docker push $(NAME):$(VERSION);

build:
	@echo "Building docker image tag: $(NAME):$(VERSION)"
	zip app.zip -q -r app -i "*.py"
	@docker build -t $(NAME):$(VERSION) .
	rm app.zip;

run:
	@echo "Running docker image tag: $(NAME):$(VERSION)"
	docker run -d -p 5000:5000 --name test $(NAME):$(VERSION);
