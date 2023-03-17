"""
Функции панели управления для приложения "Информация о пользователе".
"""

from django.contrib import admin

from person.models import Person



@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "resume",
        "github",
        "email",
    )

    # search_fields = ("title", "content")
    #
    # list_filter = (
    #     "created_at",
    #     "updated_at",
    # )