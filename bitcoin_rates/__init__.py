# load celery app when application is started
from .celery_app import app as celery_application

# __all__ = ['celery_application']
