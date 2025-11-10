from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Usar variables de entorno para producción
SECRET_KEY = config('SECRET_KEY', default='django-insecure-pin30=__f16w!3#vs$jl0%&!q%ce)b9(xmo88_^m52e232#4ac')

# SECURITY WARNING: don't run with debug turned on in production!
# En producción debe ser False
DEBUG = config('DEBUG', default=False, cast=bool)

# Configurar hosts permitidos desde variables de entorno
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [s.strip() for s in v.split(',')])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
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

ROOT_URLCONF = 'cosmofood.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [ BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'cosmofood.wsgi.application'

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.hostinger.com'
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True
#EMAIL_HOST_USER = config('EMAIL_HOST_USER')
#EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
#DEFAULT_FROM_EMAIL = 'Cosmofood <cosmofood@grivyzom.com>'
#SERVER_EMAIL = 'cosmofood@grivyzom.com'



#DEFAULT_FROM_EMAIL = f'Cosmofood <{config("EMAIL_HOST_USER")}>'

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

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Modelo de usuario personalizado
AUTH_USER_MODEL = 'core.Usuario'

# Configuración de archivos media (imágenes)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Le dice a Django cuál es la URL de tu página de login
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

# =============================================
# CONFIGURACIÓN DE SEGURIDAD PARA PRODUCCIÓN
# =============================================

# Redirigir HTTP a HTTPS en producción
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)

# Cookies seguras (solo HTTPS)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)

# CSRF Trusted Origins para producción
CSRF_TRUSTED_ORIGINS = config(
    'CSRF_TRUSTED_ORIGINS',
    default='http://localhost:8000',
    cast=lambda v: [s.strip() for s in v.split(',')]
)

# Seguridad adicional
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=0, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=False, cast=bool)

# X-Frame-Options para evitar clickjacking
X_FRAME_OPTIONS = 'DENY'

# Content Security Policy
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}
