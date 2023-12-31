# Generated by Django 5.0 on 2024-01-09 11:58

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0023_product_rating_review"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("detail", models.CharField(max_length=10000)),
                (
                    "rate",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                ("pdf", models.FileField(blank=True, null=True, upload_to="")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("cocukkitabi", "Çocuk Kitabı"),
                            ("gerilim", "Gerilim"),
                            ("macera", "Macera"),
                            ("aksiyon", "Aksiyon"),
                            ("education", "Egitim"),
                            ("biyografik", "Biyografik"),
                            ("books", "Bilim Kurgu"),
                        ],
                        default="books",
                        max_length=15,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="books",
            name="review",
        ),
        migrations.AddField(
            model_name="product",
            name="book",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="movies.book",
            ),
        ),
    ]
