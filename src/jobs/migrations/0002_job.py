import ckeditor_uploader.fields
from django.db import migrations

from typing import List


class Migration(migrations.Migration):

    dependencies: List = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="content",
            field=ckeditor_uploader.fields.RichTextUploadingField(
                default="Описание работы", verbose_name="Подробное описание работы"
            ),
        ),
    ]
