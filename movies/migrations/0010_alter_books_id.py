# Generated by Django 5.0 on 2023-12-26 16:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0009_remove_aksiyon_cat_id_remove_biyografik_cat_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="id",
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]