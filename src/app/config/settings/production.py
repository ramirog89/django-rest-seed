from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY = 'production-secret-key'
DEBUG = False
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '../persistence/database/db.sqlite3'),
#     }
# }