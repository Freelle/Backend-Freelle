# Generated by Django 5.0.6 on 2024-12-17 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_remove_user_portifolio_user_portifolio"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="projeto",
            name="image_project",
        ),
        migrations.AddField(
            model_name="projeto",
            name="foto",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="uploader.image"
            ),
        ),
    ]
