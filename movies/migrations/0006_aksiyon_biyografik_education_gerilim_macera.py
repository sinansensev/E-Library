# Generated by Django 5.0 on 2023-12-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0005_cocukkitabi"),
    ]

    operations = [
        migrations.CreateModel(
            name="aksiyon",
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
                ("name", models.CharField(max_length=80)),
                ("detail", models.CharField(max_length=1000)),
                ("review", models.CharField(max_length=1000)),
                ("rate", models.IntegerField()),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="biyografik",
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
                ("name", models.CharField(max_length=80)),
                ("detail", models.CharField(max_length=1000)),
                ("review", models.CharField(max_length=1000)),
                ("rate", models.IntegerField()),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="education",
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
                ("name", models.CharField(max_length=80)),
                ("detail", models.CharField(max_length=1000)),
                ("review", models.CharField(max_length=1000)),
                ("rate", models.IntegerField()),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="gerilim",
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
                ("name", models.CharField(max_length=80)),
                ("detail", models.CharField(max_length=1000)),
                ("review", models.CharField(max_length=1000)),
                ("rate", models.IntegerField()),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="macera",
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
                ("name", models.CharField(max_length=80)),
                ("detail", models.CharField(max_length=1000)),
                ("review", models.CharField(max_length=1000)),
                ("rate", models.IntegerField()),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
            ],
        ),
    ]
