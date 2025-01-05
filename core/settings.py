import os
import environ
from pathlib import Path
from django.db import backends
from datetime import timedelta

env = environ.Env()
environ.Env.read_env()
ENVIRONMENT = env
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
SITE_DOMAIN = os.environ.get('SITE_DOMAIN')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('SECRET_KEY')
API_WHATSAPP_WEB = os.environ.get('API_WHATSAPP_WEB')
HELP_NUMBER = os.environ.get('HELP_NUMBER')

ALLOWED_HOSTS = [
    'localhost',
    '52.15.233.227'
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000"
]

CORS_ALLOW_CREDENTIALS = True

# CSRF_COOKIE_DOMAIN = "acidjelly.com"

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000"
]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
]

PROJECT_APPS = [
    'apps.user',
    'apps.books',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
    'ckeditor',
    'ckeditor_uploader',
    'drf_yasg',
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

SITE_ID = 1

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'autoParagraph': False
    }
}

CKEDITOR_UPLOAD_PATH = "/media/"

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'core/templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_AUTH_NAME'),
#         'USER': os.environ.get('DB_AUTH_USER'),
#         'PASSWORD': os.environ.get('DB_AUTH_PASSWORD'),
#         'HOST': os.environ.get('DB_AUTH_HOST'),
#         'PORT': os.environ.get('DB_AUTH_PORT'),
#         'OPTIONS': {
#             'sslmode': 'disable', # disable SSL
#         },
#         'DISABLE_SSL': True
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'db_auth',
        'CLIENT': {
            'host': f"mongodb+srv://{os.environ.get('DB_MONGO_USER')}:{os.environ.get('DB_MONGO_PASSWORD')}@cluster0.ml6w3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
            'uuidRepresentation': 'standard',
        },
    },
    'books': {
        'ENGINE': 'djongo',
        'NAME': 'db_books',
        'CLIENT': {
            'host': f"mongodb+srv://{os.environ.get('DB_MONGO_USER')}:{os.environ.get('DB_MONGO_PASSWORD')}@cluster0.ml6w3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
            'uuidRepresentation': 'standard',
        },
    }
}

DATABASES['default']["ATOMIC_REQUEST"] = True

DATABASE_ROUTERS = [
    'apps.user.router.UserRouter',
    'apps.books.router.BooksRouter',
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 16,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ],
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(hours=10),
}

REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': 'jwt-auth',
    'JWT_AUTH_REFRESH_COOKIE': 'jwt-refresh-auth',
    'JWT_AUTH_HTTPONLY': True,
    'SESSION_LOGIN': False,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'JWT_AUTH_COOKIE_DOMAIN': '.localhost',
    'JWT_AUTH_COOKIE_SAMESITE': 'Lax',
    'LOGIN_ON_EMAIL_CONFIRMATION': False
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

REST_AUTH_SERIALIZERS = {
    'LOGIN_SERIALIZER': 'core.serializers.CustomLoginSerializer',
}

FILE_UPLOAD_PERMISSIONS = 0o640

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# if not DEBUG:
DJANGO_SERVER_EMAIL = "info@acidjelly.com"
DEFAULT_FROM_EMAIL = "Acid Jelly <info@acidjelly.com>"
EMAIL_BACKEND = env('EMAIL_BACKEND')

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

AUTH_USER_MODEL = 'user.UserAccount'

REACT_FRONT_URL = env('REACT_FRONT_URL')
DJANGO_BACK_URL = env('DJANGO_BACK_URL')