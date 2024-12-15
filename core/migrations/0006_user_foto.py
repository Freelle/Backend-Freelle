# Generated by Django 5.0.6 on 2024-12-15 22:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_alter_userprojeto_freelancer_user_and_more"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="foto",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="uploader.image",
            ),
        ),
    ]
