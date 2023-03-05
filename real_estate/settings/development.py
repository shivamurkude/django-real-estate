from .base import *

EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST=env("EMAIL_HOST")
EMAIL_USE_TLS=True
EMAIL_PORT=env("EMAIL_PORT")
EMAIL_HOST_USER=env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL="info@real-estate.com"
DOMAIN=env("DOMAIN")
SITE_NAME="Real Estate"




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