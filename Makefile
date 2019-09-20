initdb:
	python manage.py syncdb
	python manage.py migrate

install:
	pip install --upgrade setuptools
	pip install --upgrade -r requirements.txt

test:
	coverage run --source="./src/" manage.py test src
	coverage html -d coverage
	coverage erase

server:
	python manage.py runserver 0.0.0.0:7000

check:
	python manage.py check --deploy