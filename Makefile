###### VARIABLES
SOURCE_DIR = ./src/app
COVERAGE_DIR = coverage/
LOGS_DIR = logs/

DOCKER_IMAGE = python-django-starter
SERVER_PORT = 7000

local: SETTINGS = src.app.config.settings.development
dev:   SETTINGS = src.app.config.settings.development
prod:  SETTINGS = src.app.config.settings.production

####### INITIALIZATION
clean:
	# find . -name '*.pyc' -exec rm --force {}
	# find . -name '*.pyo' -exec rm --force {}
	# find . -name '*~' -exec rm --force  {}
	rm -rf $(COVERAGE_DIR)
	rm -r $(LOGS_DIR)*

install:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

####### DATABASE
initdb:
	python manage.py migrate

migrate:
	python manage.py makemigrations
	python manage.py migrate

####### RUN SERVER
.PHONY : start_server dev prod
local dev prod:
	python manage.py runserver 0.0.0.0:$(SERVER_PORT) --settings=$(SETTINGS)

####### TESTING
lint:
	flake8 $(SOURCE_DIR)

test:
	coverage run --source="$(SOURCE_DIR)" manage.py test src --force-color
	coverage html -d coverage
	coverage report -m
	coverage erase

####### BUILD / DEPLOY
check:
	python manage.py check --deploy

image-run:
	docker run -p:7000:7000 -i -t $(DOCKER_IMAGE)