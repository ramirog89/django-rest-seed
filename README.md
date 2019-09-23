django-rest-seed
===================
Working example of [django-rest-framework](https://github.com/tomchristie/django-rest-framework/tree/master) using JWTAuthentication ([rest_framework_simplejwt](https://github.com/davesque/django-rest-framework-simplejwt)) and SessionAuthentication for browseable API. Cross-Origin Resource Sharing is also enabled via [django-cors-headers](https://github.com/ottoyiu/django-cors-headers).

## Requirements 
* You should have [virtualenv](http://www.virtualenv.org/en/latest/#installation) installed. 
* Make sure your [SSH keys](https://help.github.com/articles/generating-ssh-keys) are set up properly for GitHub.

## Install 
Clone this repo, set up and activate a virtualenv:
```console
git clone git@github.com:ramirog89/django-rest-seed.git
cd django-rest-seed
virtualenv env
source env/bin/activate
```

Setup dependencies:
```console
make install
```

## Run the server 
```console
make server
```
Launch [http://localhost:7000](http://localhost:7000) in your browser.

Default **username** is `ar` and **pasword** `ar` with a preconfigured client already set up. 

**...in case** you'd like to start fresh:
```console
rm src/app/database/db.sqlite3
make initdb
```

...then head over to [Django admin](http://localhost:7000/admin/) and create your first client.

## Tests 
```console
make test 
```
