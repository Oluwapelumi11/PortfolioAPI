# Generated by Django 4.2.5 on 2023-11-16 19:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
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
                    "languages",
                    models.CharField(max_length=50, verbose_name="Languages"),
                ),
                (
                    "databases",
                    models.CharField(max_length=50, verbose_name="Databases"),
                ),
                ("tools", models.CharField(max_length=50, verbose_name="Tools")),
                ("other", models.CharField(max_length=50, verbose_name="Other")),
                (
                    "frameworks",
                    models.CharField(max_length=50, verbose_name="Frameworks"),
                ),
            ],
        ),
    ]
