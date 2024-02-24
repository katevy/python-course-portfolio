"""
Функции панели управления для приложения "Автор".
"""

from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "github_link",
        "resume_link",
        "email",
        "created_at",
        "updated_at",
    )

    search_fields = (
        "github_link",
        "resume_link",
        "email",
    )

    list_filter = (
        "created_at",
        "updated_at",
    )
