"""
Django settings for boty / Valyout /project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://boty github aqui

"""

from pathlib import Path
import os
from django.contrib.messages import constants as mensajesError

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u8@!bt1^lt^(4kre4l_@oige@j$_mcorfvahva^)iiu059coy!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['botyvalyout.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'usuariosApp',
    'noticiaApp',
    'tiendaApp',
    'botyApp',
    'freemiumApp',
    'crispy_forms',
    'botlogicApp',
    'carro',
    'botybtc1mApp',
    'criptoApp',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'botapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'carro.context_processor.importe_total_carro',
            ],
        },
    },
]

WSGI_APPLICATION = 'botapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

#LANGUAGE_CODE = 'es'
LANGUAGE_CODE = 'es-eu'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

#Config CORS
#AUTH_USER_MODEL = 'users.User'
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# configuracion email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST= "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = "soporteboty@gmail.com"
EMAIL_HOST_PASSWORD=''

# Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Mensajes de error

MESSAGE_TAGS = {

    mensajesError.DEBUG: 'debug',
    mensajesError.INFO: 'info',
    mensajesError.SUCCESS: 'success',
    mensajesError.WARNING: 'warning',
    mensajesError.ERROR: 'danger',

}

# botlogic $$

#  CONEXION datos Binance
API_KEY = "5DEbjdicxFUBui1MksOKPSFolRWWRVXjFD6OdGfIOFJ6Dh6CHsbhPoCsbITjChor"
API_SECRET_KEY = "AyYhAD5vSUQibFl4gC1TWAH6GoaHdq1Rc8xSMPPn85w8CcxDzcDhBAOdoODH5P7f"

#  CONEXION mensajes Telegram BOT
bot_token = '5326927177:AAEyFNh5jcHPzJGw4dEw1xmttpchqxxFNXY'
bot_chatID = '993513446'

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())



