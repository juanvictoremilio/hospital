from .base import *
DEBUG = False
ADMINS = (
    ('Víctor Sánchez', 'direccion@amcare.com-mx'),
)
ALLOWED_HOSTS = ['*eskvlapivs.com', 'www.aeskvlapivs.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aeskvlapivs',
        'USER': 'postgres',
        'PASSWORD': 'ayla122333',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
        }
}

