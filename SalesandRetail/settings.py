"""
Django settings for SalesandRetail project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e8ev*est#_cq*80$z-oxd9o9id)o1ki+lsfn3$qb2wv#o(d1(^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS = [
    'users',
    'inventory',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoise.MiddleWare',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'SalesandRetail.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates',BASE_DIR / 'users/templates'],
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

WSGI_APPLICATION = 'SalesandRetail.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/


MEDIA_ROOT=(BASE_DIR / 'media' / 'profile_images')


MEDIA_URL='/media/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR/'media'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'abhishekkumbhar005@gmail.com'
EMAIL_HOST_PASSWORD = 'vgox lfcm oeek pxeq'
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"














































# from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
# from .models import *
# from django.http import JsonResponse
# from django.db.models import F,Q,Sum,Avg
# from django.contrib import messages
# from datetime import datetime, timedelta
# from decimal import Decimal
# import plotly.graph_objs as go
# # import plotlib
# # Create your views here. 
# from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
# from .models import *
# from django.http import JsonResponse
# from django.db.models import F,Q,Sum,Avg
# from django.contrib import messages
# from datetime import datetime, timedelta
# from decimal import Decimal
# import plotly.graph_objs as go
# # import plotlib
# # Create your views here. 
# from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
# from .models import *
# from django.http import JsonResponse
# from django.db.models import F,Q,Sum,Avg
# from django.contrib import messages
# from datetime import datetime, timedelta
# from decimal import Decimal
# import plotly.graph_objs as go
# # import plotlib
# # Create your views here. 


# from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate
# from .models import *
# from django.http import JsonResponse
# from django.db.models import F,Q,Sum,Avg
# from django.contrib import messages
# from datetime import datetime, timedelta
# from decimal import Decimal
# import plotly.graph_objs as go
# # import plotlib
# # Create your views here. 