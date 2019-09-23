NAME="service/flask/template"
VERSION=0.0.1

help:
	@echo "help"
	@echo "tag"
	@echo "push"
	@echo "build"
	@echo "run"
	@echo "all"

tag:
	@echo "Tagging docker image tag: $(tag)"
	docker tag $(NAME):$(VERSION) $(NAME):latest

push:
	@echo "pushing docker image tag: $(tag)"
	docker push $(NAME):latest

build:
	tag="$(NAME):$(VERSION)"
	@echo "Building docker image tag: $(tag)"
	zip app.zip -q -r app -i "*.py"
	docker build -t $tag .
	rm app.zip;

run:
	@echo "Running docker image tag: $(tag)"
	docker run -d -p 5000:5000 --name test ${tag};

all: build push
