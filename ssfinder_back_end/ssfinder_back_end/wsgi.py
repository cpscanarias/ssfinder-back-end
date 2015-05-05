"""
WSGI config for ssfinder_back_end project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
import site

from django.core.wsgi import get_wsgi_application


#site.addsitedir('/opt/virtualenvs/ssfinder/lib/python2.7/site-packages')

#sys.path.append('/django_projects/ssfinder_back_end/ssfinder_back_end')
#sys.path.append('/django_projects/ssfinder_back_end/ssfinder_back_end/ssfinder_back_end')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ssfinder_back_end.settings")

# Activate your virtual env
#activate_env=os.path.expanduser('/opt/virtualenvs/ssfinder/bin/activate_this.py')
#execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
