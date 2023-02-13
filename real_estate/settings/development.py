from .base import *

DATABASES = {
   

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("DJANGO_POSTGRES_DATABASE"),
        'USER': env("DJANGO_POSTGRES_USER"),
        'PASSWORD': env("DJANGO_POSTGRES_PASSWORD"),
        'HOST': env("DJANGO_POSTGRES_HOST"),
        'PORT': env("DJANGO_POSTGRES_PORT"),
    },
}