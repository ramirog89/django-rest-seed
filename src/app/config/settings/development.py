from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*_jxj=m9p5c0&_58w4()7yb4d*_bu8+jv(=i=$$wc2hku7k3r5'
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../persistence/database/db.sqlite3'),
    }
}

# POSTGRES..
# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.postgresql',
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'qqxbkrjl',
#         'USER': 'qqxbkrjl',
#         'PASSWORD': '9boHUg7Yxa-SL-g1OyDAdcODqX8TqKD6',
#         'HOST': 'salt.db.elephantsql.com',
#         'PORT': '5432'
#     }
# }