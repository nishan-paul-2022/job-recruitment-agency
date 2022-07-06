import os
import os.path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-5zq=wq0(m(s^j45(zgp$&q96bh3s3-3o=5+kx+$ho=zf$92fp7'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'done_backend_ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'{BASE_DIR}/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

WSGI_APPLICATION = 'done_backend_ecommerce.wsgi.application'

DATABASES = {
    'default': {
        # OPTION 1
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': f'{BASE_DIR}/db.sqlite3'

        # OPTION 2
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': '19_done_backend_ecommerce',
        # 'USER': 'root',
        # 'PASSWORD': '',
        # 'HOST': '127.0.0.1',
        # 'PORT': ''

        # OPTION 3
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': '8k3RtDN1QB',
        # 'USER': '8k3RtDN1QB',
        # 'PASSWORD': 'vuGcCG3jWa',
        # 'HOST': 'remotemysql.com',
        # 'PORT': '3306'

        # OPTION 4
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': '19_done_backend_ecommerce',
        # 'USER': 'postgres',
        # 'PASSWORD': 'nishan',
        # 'HOST': 'localhost',
        # 'PORT': '5432'

        # OPTION 5
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd961i1fl8kjeuh',
        'USER': 'uibfgjftenrglm',
        'PASSWORD': '7a2342608d7faed6943b7461804d6fa7f18db846efbc7f377b7496176954925d',
        'HOST': 'ec2-3-228-78-248.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'