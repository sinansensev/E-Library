# Generated by Django 5.0 on 2023-12-26 17:38

import movies.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0014_alter_books_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cocukkitabi",
            name="id",
            field=models.PositiveBigIntegerField(
                default=movies.models.generate_custom_idcocuk,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
