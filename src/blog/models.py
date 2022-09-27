from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from base.models import TimeStampMixin


class Blog(TimeStampMixin):
    """
    Модель для хранения сообщений блога.
    """

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = RichTextUploadingField(verbose_name="Содержимое сообщения")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    publication_date = models.DateTimeField(verbose_name="Дата публикации")

    class Meta:
        verbose_name = "Сообщение блога"
        verbose_name_plural = "Сообщения блога"

    def __str__(self) -> str:
        return f'Объект "Сообщение блога" (id={self.pk})'

    def summary(self) -> str:
        """
        Краткое содержание сообщения.

        :return:
        """

        return self.content[:100] + "..."

    def publication_date_format(self) -> str:
        """
        Форматирование даты публикации.

        :return:
        """

        return self.publication_date.strftime("%b %e %Y")
