from typing import List

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: List = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("github_link", models.URLField(verbose_name="Ссылка Github")),
                ("resume_link", models.URLField(verbose_name="Ссылка на резюме")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
            ],
            options={
                "verbose_name": "Автор",
                "verbose_name_plural": "Авторы",
            },
        ),
    ]
