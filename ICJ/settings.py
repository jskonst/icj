# -*- coding=utf8 -*-

# Standart settings import
from default_settings import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',   # Add 'postgresql_psycopg2',  'mysql',  'sqlite3' or 'oracle'.
        'NAME': os.path.join(os.path.dirname(__file__), 'mydata.db').replace('\\', '/'),  # Or path to database file if using sqlite3.
        'USER': '',  # 'ivpy',                      # Not used with sqlite3.
        'PASSWORD': '',  # 'tf0uqJidWtfYoDZraM',                  # Not used with sqlite3.
        'HOST': '',  # 'ivpy.ru',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = '-7f8#vqiqjx0ke6sjj^!j2)82901_ehaogwaxfsu6%xiplrx7q'

ACCOUNT_ACTIVATION_DAYS = 2  # кол-во дней для хранения кода активации
# для отправки кода активации
AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = 'admin@icj.konstructor.ru'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'admin@icj.konstructor.ru'
