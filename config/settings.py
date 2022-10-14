"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# ========================== DEV VERSION(AWS) ============================================
secret_file = os.path.join(BASE_DIR, 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")
# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True
AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_secret("AWS_SECRET_ACCESS_KEY")

# ========================= DEPLOY VERSION(HEROKU) =============================================

# SECRET_KEY = config('SECRET_KEY')
# # DEBUG = config('DEBUG', default=False, cast=bool)
# DEBUG = True # 일단 테스트
# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

# ========================= AWS Settings ===============================================
AWS_STORAGE_BUCKET_NAME = 'jinhyung.test.aws'
AWS_REGION = 'ap-northeast-2'

IMAGE_URL = "https://s3.%s.amazonaws.com/%s" % (AWS_REGION, AWS_STORAGE_BUCKET_NAME)


ALLOWED_HOSTS = [
    'nuseum-v2.herokuapp.com',
    '127.0.0.1',
    'localhost',
    '0.0.0.0',
    '.ap-northeast-2.compute.amazonaws.com',
    '.nuseum.site'
    ]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'storages',
    'corsheaders',
    # my apps
    'consumptions',
    'foods',
    'accounts',
    'qnas',
    'notices',
]

# rest_framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated', # 기본으로 인증된 유저만 API에 접근가능
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}
# rest_auth customizing
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

# Auth User
AUTH_USER_MODEL = 'accounts.User'

# JWT

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth'  # test
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'

from datetime import timedelta

SIMPLE_JWT = {
    # deploy
    'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME' : timedelta(hours=1),
    # test
    # 'ACCESS_TOKEN_LIFETIME' : timedelta(minutes=2),
    # 'REFRESH_TOKEN_LIFETIME' : timedelta(minutes=1),
    'ROTATE_REFRESH_TOKENS' : False, # refresh token 재발급 X
    # 'ROTATE_REFRESH_TOKENS' : True, # refresh token 재발급 O
    'BLACKLIST_AFTER_ROTATION' : True, # Blacklist 관련 설정
    "TOKEN_REFRESH_SERIALIZER": "accounts.serializers.CustomTokenRefreshSerializer", # custom token refresh
}

# 쿠키 TEST
JWT_AUTH_SAMESITE = 'None'
JWT_AUTH_SECURE = True
CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

# ALLAUTH
# SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.security.SecurityMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# CORS 설정
CORS_ORIGIN_WHITELIST = [
                        'https://nuseum-rho.vercel.app',
                        'https://nuseum-949i9v22k-parkjju.vercel.app',
                        'http://127.0.0.1:3000',
                        'http://localhost:3000',
                        'https://dev.example.com:3000',
                        'https://nuseum-fnqo.vercel.app',
                        'https://nuseum-admin.vercel.app']
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# AWS DB SETTING
# import pymysql
# pymysql.install_as_MySQLdb()

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "nuseum", 
#         "USER": "jinhyung",
#         "PASSWORD": get_secret("AWS_RDS_PASSWORD"),
#         "HOST": "database-1.cbtkoz4oqhvu.ap-northeast-2.rds.amazonaws.com",
#         "PORT": "3306",
#         "OPTIONS": {
#             "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"
#         }
#     }
# }

# HEROKU DB SETTING
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "ko"
# LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"
# TIME_ZONE = "UTC"

USE_I18N = True

# USE_TZ = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)