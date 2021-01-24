IMAGE := api-template:latest
CONTAINER := api-template-server

launch-dev:
	@python api/server.py

build:
	@docker build -t $(IMAGE) .

launch:
	@docker run -d -p 5000:5000 --name $(CONTAINER) $(IMAGE) 

.PHONY: launch-dev build launch
