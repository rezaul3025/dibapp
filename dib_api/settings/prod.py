from dib_api.settings.common import  *
import os

DEBUG = True

SUMMER_TIME_DIF = 0

HOST = 'https://prayer.darulihsan-berlin.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASS'],
        'HOST': os.environ['DATABASE_HOST'],
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
        'TIME_ZONE': 'Europe/Berlin',
    }
}