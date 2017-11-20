"""
Django settings for gettingstarted project, on Heroku. For more info, see:
https://github.com/heroku/heroku-django-template

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: change this before deploying to production!
#SECRET_KEY = 'i+acxn5(akgsn!sr4^qgf(^m&*@+g1@u^t@=8s@axc41ml*f=s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#TEST_RUNNER = 'gettingstarted.heroku_test_runner.HerokuDiscoverRunner'


# Application definition

#INSTALLED_APPS = (
 #   'django.contrib.admin',
  #  'django.contrib.auth',
   # 'django.contrib.contenttypes',
    #'django.contrib.sessions',
    #'django.contrib.messages',
    #'django.contrib.staticfiles',
    #'hello'
#)

#MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
 #   'whitenoise.middleware.WhiteNoiseMiddleware',
  #  'django.contrib.sessions.middleware.SessionMiddleware',
 #  'django.middleware.common.CommonMiddleware',
  #  'django.middleware.csrf.CsrfViewMiddleware',
  #  'django.contrib.auth.middleware.AuthenticationMiddleware',
  #  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  #  'django.contrib.messages.middleware.MessageMiddleware',
  # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
  #  'django.middleware.security.SecurityMiddleware',
#)

ROOT_URLCONF = 'delbot.urls'

#TEMPLATES = [
 #   {
 #       'BACKEND': 'django.template.backends.django.DjangoTemplates',
 #       'DIRS': [],
 #       'APP_DIRS': True,
 #       'OPTIONS': {
 #           'debug': True,
  #          'context_processors': [
   #             'django.template.context_processors.debug',
   #             'django.template.context_processors.request',
   #             'django.contrib.auth.context_processors.auth',
   #             'django.contrib.messages.context_processors.messages',
   #         ],
   #     },
   # },
#]

WSGI_APPLICATION = 'delbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #   }
#}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

#AUTH_PASSWORD_VALIDATORS = [
 #   {
 #       'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
 #   },
 #   {
 #       'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
 #   },
 #   {
 #       'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
 #   },
 #   {
 #       'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
 #   },
#]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/


# Allow all host headers
ALLOWED_HOSTS = ['*']

