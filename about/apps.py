from django.apps import AppConfig
from .models import About

class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
