"""
Django settings for project.

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ADMINS = (
    ('Salvador', 'salvador.mrf@gmail.com'),
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9y2k_3dpa$qxuzbt-t#$3q3hjp#$^kmz)$n^li9adn0yod^_g&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'projectapps.coreadmin',
    'projectapps.core',
    'projectapps.images',
    'projectapps.documents',
    'projectapps.tags',
    'projectapps.pages',
    'projectapps.articles',
    'projectapps.users',
    'projectapps.settings',
    'projectapps.tasks',
    'projectapps.web',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',
)

ROOT_URLCONF = 'project.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_VERSION = os.environ.get('STATIC_VERSION', '0.0.0')
STATIC_URL = '/static/v{0}/'.format(STATIC_VERSION)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Security

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'
SECURE_FRAME_DENY = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 2592000  # 30 days
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # App Engine doesn't use HTTPS internally, so the /_ah/.* URLs need to be exempt.
    # djangosecure compares these to request.path.lstrip("/"), hence the lack
    # of preceding /
    r"^_ah/",
    # cron must be insecure because it's called insecurely
    r"^_cron/"
]

# CSP settings
#
# Enable CSP directives on /admin
# Admin path (/admin) is by default exempt on django-csp (CSP_EXCLUDE_URL_PREFIXES)
# https://github.com/mozilla/django-csp/blob/master/csp/middleware.py#L22
# CSP_EXCLUDE_URL_PREFIXES = ()

# Exclude admin from CSP for demo simplicity
CSP_EXCLUDE_URL_PREFIXES = ('/admin',)

CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'",)
CSP_FRAME_SRC = ("'self'",)
CSP_IMG_SRC = ("'self'", "data:", "storage.googleapis.com",)
CSP_STYLE_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", "*.gstatic.com",)
CSP_CONNECT_SRC = ("'self'",)
CSP_MEDIA_SRC = ("'self'", "storage.googleapis.com",)
