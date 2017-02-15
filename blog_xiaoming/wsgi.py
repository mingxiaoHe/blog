"""
WSGI config for blog_xiaoming project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
#sys.path.append('/var/www/blog_xiaoming/')
#sys.path.append('/var/www/blog_xiaoming/blog_xiaoming/')
#print sys.path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog_xiaoming.settings")

application = get_wsgi_application()
