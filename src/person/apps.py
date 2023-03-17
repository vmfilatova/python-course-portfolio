from django.apps import AppConfig


class PersonConfig(AppConfig):
    """
    Конфигурация приложения.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "person"
    verbose_name = "Информация о пользователе"