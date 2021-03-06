# -*- coding: utf-8 -*-
"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 1.8.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2_6_8kc@=y2tqjq-ce$nss1n5k7zdjymk6fr0g-p&g5rmn!h7d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'myproject',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #fix for bug1
    'django.contrib.staticfiles',
)
#fix for bug1
STATICFILES_FINDERS =(
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


#STATIC_ROOT = os.path.join(BASE_DIR,'static')

#fix for bug1
STATICFILES_DIRS = (

    os.path.join(BASE_DIR,'static'),
)

STATIC_ROOT = '/static/'



ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates').replace('\\','/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
		        'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #fix for bug1
                'django.core.context_processors.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

FILE_CHARSET = 'utf-8'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

def database_setting(enviroment):
    if enviroment=="production":
        connect_options = {
            'default': {'ENGINE': 'django.db.backends.mysql','NAME': 'blogdb','USER': '*****','PASSWORD': '*******','HOST': '127.0.0.1','PORT': '3306',}}
    else:
        connect_options = {
            'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR,'sqlite.db'),}
        }
    return connect_options

#РїСЂРё СѓСЃС‚Р°РЅРѕРІРєРµ РЅР° РїСЂРѕРґСѓРєС‚РёРІ РЅСѓР¶РЅРѕ РјРµРЅСЏС‚СЊ РЅР° "production"
DATABASES = database_setting("test")



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
