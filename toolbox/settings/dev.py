from toolbox.settings.base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': env.db()
}

CORS_ALLOWED_ORIGINS = ['http://127.0.0.1']
