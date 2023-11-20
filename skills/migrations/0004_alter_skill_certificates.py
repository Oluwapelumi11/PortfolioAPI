# Generated by Django 4.2.5 on 2023-11-16 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("skills", "0003_alter_skill_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="skill",
            name="certificates",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="skills.certification",
                verbose_name="Certificates",
            ),
        ),
    ]