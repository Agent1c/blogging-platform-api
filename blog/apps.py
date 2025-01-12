from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'


    def ready(self):
        # Place your startup code here
        from . import signals  # Example of importing signals
        from django.dispatch import receiver
