from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from base.models import TimeStampMixin


class Person(TimeStampMixin):
    """
        Модель для информации о пользователе.
        """
    resume = models.CharField(max_length=255, verbose_name="Резюме")
    github = models.CharField(max_length=255, verbose_name="GitHub")
    email = models.CharField(max_length=255, verbose_name="Электронная почта")

    class Meta:
        verbose_name = "Информация о пользователе"
        verbose_name_plural = "Информация о пользователях"

    def __str__(self) -> str:
        return f'Объект "Информация о пользователе" (id={self.pk})'
