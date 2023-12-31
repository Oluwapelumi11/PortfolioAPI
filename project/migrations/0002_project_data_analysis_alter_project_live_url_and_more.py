# Generated by Django 4.2.5 on 2023-11-16 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0002_certification_remove_skill_databases_and_more"),
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="data_analysis",
            field=models.BooleanField(null=True, verbose_name="Data Analysis"),
        ),
        migrations.AlterField(
            model_name="project",
            name="live_url",
            field=models.URLField(null=True, verbose_name="Url"),
        ),
        migrations.RemoveField(
            model_name="project",
            name="skills",
        ),
        migrations.AddField(
            model_name="project",
            name="skills",
            field=models.ManyToManyField(to="skills.skill", verbose_name="Skills"),
        ),
    ]
