"""
Функции панели управления для приложения "Блог".
"""

from django.contrib import admin

from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "publication_date",
        "created_at",
        "updated_at",
    )

    search_fields = ("title", "content")

    list_filter = (
        "created_at",
        "updated_at",
    )
