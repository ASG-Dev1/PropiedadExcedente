"""
Django settings for PropiedadExcedente project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# HINT: ESTA ES LA CONFIGURACIÓN DEL EMAIL #
# YA QUE ESTÁN AQUÍ NO SE OLVIDEN DE DESLIZAR YA QUE EN LA PARTE INFERIOR TENDRÁN LA PARTE MÁS IMPORTANTE DEL PROYECTO #
# WARNING: EL INVITE NO LLEGARÁ, O TIRARÁ ERROR PORQUE LA CONFIGURACIÓN ESTA VACÍA #
# HINT: BUSQUEN COMO CONFIGURARLO EN SU GMAIL #
# HINT: HAY UNA MANERA SEGURA DE ESCONDERLOS, CUANDO LLEGUEN A LA CONFIGUACIÓN DE AZURE DEBERÁN HACERLO #
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True 
EMAIL_HOST_USER =  ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m@@9-)$$miys#dut56aw)+5n%(vph=1avr-l5yvc2s24irv8vd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Inventario',
    'Landing',
    'Usuarios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PropiedadExcedente.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
            ],
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

WSGI_APPLICATION = 'PropiedadExcedente.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),

]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

AUTH_USER_MODEL = 'Usuarios.Usuario'



# WARNING: LA PARTE MÁS IMPORTANTE DEL PROYECTO ES ESTA #
# BUSQUEN BASTANTE INFORMACIÓN Y VAYAN CONFIGURANDO BIEN CON TIEMPO #

# AZURE CONFIGURATIONS #

# ALLOWED_HOSTS = ['*','https://prodis.azurewebsites.net','https://prodis-staging.azurewebsites.net','https://prodisdev.azurewebsites.net']

# CSRF_TRUSTED_ORIGINS = ['http://*.127.0.0.1',
#                         'https://prodis.azurewebsites.net', 'https://prodisdev-staging.azurewebsites.net','https://prodisdev.azurewebsites.net','https://prodis-staging.azurewebsites.net']

#     else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.environ.get('DJANGO_DB_NAME'),
#             'USER': os.environ.get('DJANGO_DB_USER'),
#             'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
#             'HOST': os.environ.get('DJANGO_DB_HOST'),
#             'PORT': os.environ.get('DJANGO_DB_PORT'),
#             'OPTIONS': {'sslmode': 'require', },
#         }
#     }
    
#     else: 
#     DEFAULT_FILE_STORAGE = 'DEPO.az_config.AzureMediaStorage'
#     STATICFILES_STORAGE = 'DEPO.az_config.AzureStaticStorage'

#     AZURE_STORAGE_KEY = os.environ.get('AZURE_STORAGE_KEY', False)
#     AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME')
#     AZURE_MEDIA_CONTAINER = os.environ.get('AZURE_MEDIA_CONTAINER', 'media')
#     AZURE_STATIC_CONTAINER = os.environ.get('AZURE_STATIC_CONTAINER', 'staticc')
#     AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.azureedge.net'  # CDN URL
#     # AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'  # Files URL

#     STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'
#     MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'
    
#     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
