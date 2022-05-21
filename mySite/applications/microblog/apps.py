from django.apps import AppConfig


class MicroblogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "microblog"
    verbose_name = "Микроблог"

    def ready(self):
        import microblog.signals
