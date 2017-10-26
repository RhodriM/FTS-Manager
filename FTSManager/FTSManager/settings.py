"""
Django settings for FTSManager project.

Generated by 'django-admin startproject' using Django 1.9.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType, LDAPSearchUnion
import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rvq#d8*vm+!1cx4^lj^-)6hlbksqo1o+pgr+9h*%y8$ge50+8^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("FTS_DEBUG", False)

ALLOWED_HOSTS = ['satan.cs.cf.ac.uk', 'localhost', 'fts.cs.cf.ac.uk', 'fts']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dal',
    'dal_select2',
    'kronos',
    'events',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FTSManager.urls'

TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
},
]

WSGI_APPLICATION = 'FTSManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': 'cspg.cs.cf.ac.uk',
            'PORT': '5432',
        }
    }



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://ldap.cs.cf.ac.uk:389"

MAIN_DN = "dc=cs,dc=cardiff.ac.uk"
USERS_DN = "ou=People,"+MAIN_DN
GROUPS_DN = "ou=Group,"+MAIN_DN

AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,"+USERS_DN

AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email": "mail"}

AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_GROUP_SEARCH = LDAPSearchUnion(
    LDAPSearch(GROUPS_DN, ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)"),
)


# SUPERUSERS/ADMINS ARE DEFINED HERE.
STAFF = ["c1106886", "c1009692"]
SUPERUSERS = ["c1106886", "c1009692"]

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_staff": ["cn={0},{1}".format(st, GROUPS_DN) for st in set(STAFF+SUPERUSERS)],
    "is_superuser": ["cn={0},{1}".format(st, GROUPS_DN) for st in SUPERUSERS],
}


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

EMAIL_HOST = os.getenv("SMTP_SERVER", "portico.cs.cf.ac.uk")
EMAIL_PORT = os.getenv("SMTP_PORT", 465)
EMAIL_USE_SSL = os.getenv("SMTP_SSL", "True").lower() in ('1', "true")

if not DEBUG:
    STATIC_ROOT = "/usr/src/app/FTSManager/static" # Change this to a directory that is being served as /static/ by your web server
