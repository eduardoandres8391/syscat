"""
Django settings for SYSCAT project.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
#from mongoengine import register_connection
#from mongoengine import connect
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
'django.core.context_processors.request',
)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l3q^u@i75a45#^xy89ktl!i@l5sbdyavxx(a%sgw6f=rmcxmqi'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['*']
# Application definition
INSTALLED_APPS = (
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'app',
)
MIDDLEWARE_CLASSES = (
'django.contrib.sessions.middleware.SessionMiddleware',
'django.middleware.common.CommonMiddleware',
#'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
ROOT_URLCONF = 'SYSCAT.urls'
WSGI_APPLICATION = 'SYSCAT.wsgi.application'
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.dummy'
# }
#}
#try:
#register_connection(alias='default',name='syscat')
#connection = connect('default', alias='syscat')
#print "Conectado"
#connection.disconnect();
#except Exception as e:
#print "Error al Conectar con la base de datos", type(e), e
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = '/'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
os.path.join(BASE_DIR, "static"),
)
TEMPLATE_DIRS = ('%s/'% BASE_DIR,)