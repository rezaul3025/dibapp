from dib_api.settings.common import  *

DEBUG = True

SUMMER_TIME_DIF = 0

HOST = 'https://prayer.darulihsan-berlin.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dibevents',
        'USER': 'dibevents',
        'PASSWORD': '@Akm8@cwp9*',
        'HOST': '160.153.155.4',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
        'TIME_ZONE': 'Europe/Berlin',
    }
}