"""
Django settings for food_store project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3z*hbhh464(cqji$r@n+)r2x-3%ul7!#x#v6knk+age7ma9n+l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'autofixture',
    'sales',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'food_store.urls'

WSGI_APPLICATION = 'food_store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# MySQL on Mac OS X: http://www.macminivault.com/mysql-mountain-lion/
# http://stackoverflow.com/questions/4559699/python-mysqldb-and-library-not-loaded-libmysqlclient-16-dylib
# Other options for MAMP: https://racingtadpole.com/blog/mamp-python-and-mysqldb/
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'food_store',
        'USER': 'root',
        'PASSWORD': '',
        'HOST' : '127.0.0.1'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
# Path Media files for Develop
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# constant for handling routes for pictures of the fixtures
TEST_IMAGES_SALES_APP = os.path.join(BASE_DIR, 'sales/fixtures/images')
