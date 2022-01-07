from django.apps import AppConfig


class MylistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myList'
    verbose_name = 'Мой список'

    def ready(self):
        import myList.signals