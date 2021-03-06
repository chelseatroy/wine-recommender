# import os
#
# # This application object is used by the development server
# # as well as any WSGI server configured to use this file.
# import django.core.handlers.wsgi
#
# application = django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")
application = Cling(get_wsgi_application())