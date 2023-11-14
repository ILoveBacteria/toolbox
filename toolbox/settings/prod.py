from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

database_url = env.db()
database_url['CONN_MAX_AGE'] = 600
DATABASES = {
    'default': database_url
}

CORS_ALLOWED_ORIGINS = env('CORS_ALLOWED_ORIGINS', cast=list)

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_CONTENT_TYPE_NOSNIFF = True
