from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения информации об авторе.
    """

    email = models.EmailField(max_length=254, verbose_name="Email")
    github_link = models.URLField(verbose_name="Ссылка Github")
    resume_link = models.URLField(verbose_name="Ссылка на резюме")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f"Автор (id={self.pk})"
