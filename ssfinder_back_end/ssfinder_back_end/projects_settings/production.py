from .secret import *

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['www.robotclip.org']

STATIC_ROOT = '/django_projects/ssfinder_back_end/ssfinder_back_end/ssfinder_back_end/static/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
