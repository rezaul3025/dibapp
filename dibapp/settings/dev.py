from dibapp.settings.common import  *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SUMMER_TIME_DIF = 0

HOST = 'http://127.0.0.1:8000'

#TIME_ZONE : 'Europe/Berlin'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dib_api',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'dev_mysql',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'},
        #'TIME_ZONE': 'Europe/Berlin',
    }
}


#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.mysql',
 #       'NAME': 'dibevents',
 #       'USER': 'dibevents',
 #       'PASSWORD': '@Akm8@cwp9*',
 #       'HOST': '160.153.155.4',
 #       'PORT': '3306',
 #       'OPTIONS': {'charset': 'utf8mb4'},
 #   }
#}