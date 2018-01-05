from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.setdefault('DJANGO_DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.setdefault('DJANGO_DB_NAME', ''),
        'USER': os.environ.setdefault('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.setdefault('DJANGO_DB_PASSWORD', ''),
        'HOST': os.environ.setdefault('DJANGO_DB_HOST', ''),
        'PORT': os.environ.setdefault('DJANGO_DB_PORT', ''),
    }
}
