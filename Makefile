.PHONY : start_server dev prod

initdb:
	python manage.py migrate

migrate:
	python manage.py makemigrations
	python manage.py migrate

clean:
	# find . -name '*.pyc' -exec rm --force {}
	# find . -name '*.pyo' -exec rm --force {}
	# find . -name '*~' -exec rm --force  {}
	rm -rf coverage/
	rm -r logs/*
	rm -rf *.egg-info

createdatabase:
	docker mysql

databaserun:
	docker run mysql

install:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

test:
	coverage run --source="./src/app" manage.py test src --force-color
	coverage html -d coverage
	coverage report -m
	coverage erase

local: SETTINGS = src.app.config.env.development
dev:   SETTINGS = src.app.config.env.development
prod:  SETTINGS = src.app.config.env.production

local dev prod:
	python manage.py runserver 0.0.0.0:7000 --settings=$(SETTINGS)

check:
	python manage.py check --deploy

docker-run:
	docker build \
		--file=./Dockerfile \
		--tag=rest_app ./
	docker run \
		--detach=false \
		--name=rest_app \
		--publish=$(HOST):8080 \
		rest_app