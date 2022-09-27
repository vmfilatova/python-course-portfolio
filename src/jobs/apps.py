from django.apps import AppConfig


class JobsConfig(AppConfig):
    """
    Конфигурация приложения.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "jobs"
    verbose_name = "Работы для портфолио"
