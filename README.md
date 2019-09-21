# DJANGO PLUGINS
DJANGO REST FRAMEWORK
https://www.django-rest-framework.org/

# DJANGO JWT AUTH 
DJANGO JWT Auth Token PLUGIN for REST_FRAMEWORK
https://github.com/davesque/django-rest-framework-simplejwt

# SWAGGER - drf-yasg
1 https://github.com/axnsan12/drf-yasg#installation
2 https://drf-yasg.readthedocs.io/en/stable/security.html -> config

# MIDDLEARES
https://simpleisbetterthancomplex.com/tutorial/2016/07/18/how-to-create-a-custom-django-middleware.html
https://uniwebsidad.com/libros/django-1-0/capitulo-15/que-sigue-15
# SERVICES + BUSINESS LOGIC
https://mitchel.me/2017/django-service-objects/
https://django-service-objects.readthedocs.io/en/latest/
https://medium.com/@jairvercosa/business-logic-in-django-projects-7fe700db9b0a

# PA LEER:
1 https://medium.com/backticks-tildes/lets-build-an-api-with-django-rest-framework-part-2-cfb87e2c8a6c

2 https://dzone.com/articles/restful-api-authentication-basics-1

# Covereage report / testing
https://coverage.readthedocs.io/en/v4.5.x/cmd.html#execution
https://docs.djangoproject.com/en/2.2/topics/testing/advanced/#testing-reusable-applications
https://medium.com/sulang/testing-django-rest-framework-d98279a5d3a5
- Colores en los tests...?
 Red green unit test: https://github.com/stevematney/redgreenunittests

# MAKEFILE
https://krzysztofzuraw.com/blog/2016/makefiles-in-python-projects.html

# SETUP.py?
https://lincolnloop.com/blog/using-setuppy-your-django-project/

# Deploy Prod
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

# PoC:
- Registrar un CRUD con endpoints privados/protegidos con errores estandares
- Swagger + JWT Token
- Authorization con JWT
- DATABASE manager
- PIP setup via requirements (todas las dependencias necesrarias)
- Dejar un readme con el setup del seed y como crear routes
- Poner un ORM?.. algo asi? que onda (postgres/msyql/sqlite?)
  - Migrations?
- Internationalization? (multilanguage... setup)
- Testing
  - Automation? how to run all test as part of CI
  - Makefile .. ?
- Deploy Production?
  - Setup.cfg / Setup.py ?
- Multiple environment config files.. ? 



me gusta el README de aca
https://github.com/erkarl/django-rest-framework-oauth2-provider-example

# Siguientes pasos
Implementar los Servicios para la abstraccion de logica de negocios
Crear el ABM de usuarios
Crear ABM de tags
Relacion 1 a 1 post - user
Relacion n a n post - tags
Plan bien definido de migraciones
Como se hacen bien de 0 y cada cambio como se realiza correctamente.