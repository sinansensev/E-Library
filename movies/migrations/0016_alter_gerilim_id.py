# Generated by Django 5.0 on 2023-12-26 17:40

import movies.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0015_alter_cocukkitabi_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gerilim",
            name="id",
            field=models.PositiveBigIntegerField(
                default=movies.models.generate_custom_idgerilim,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]