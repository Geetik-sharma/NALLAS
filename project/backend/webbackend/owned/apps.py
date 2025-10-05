from django.apps import AppConfig


class OwnedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'owned'
