from .base import *

DEBUG = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
# CSRF_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = False
USE_X_FORWARDED_HOST = True

ALLOWED_HOSTS = ['syah-dev.eu-west-1.elasticbeanstalk.com', 'localhost']

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }

STATIC_ROOT = os.path.join(BASE_DIR, "..", "www", "static")
STATIC_URL = '/static/'
