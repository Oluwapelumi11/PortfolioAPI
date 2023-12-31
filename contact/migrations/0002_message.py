# Generated by Django 4.2.5 on 2023-12-03 02:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contact", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("message", models.TextField(verbose_name="message")),
            ],
        ),
    ]
