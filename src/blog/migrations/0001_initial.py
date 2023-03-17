# Generated by Django 4.1.1 on 2022-09-20 15:45
from typing import List

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                ("content", models.TextField(default=0,verbose_name="Содержимое сообщения")),
                (
                    "image",
                    models.ImageField(upload_to="images/", verbose_name="Изображение"),
                ),
                (
                    "publication_date",
                    models.DateTimeField(verbose_name="Дата публикации"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
