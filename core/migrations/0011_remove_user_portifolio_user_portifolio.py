# Generated by Django 5.0.6 on 2024-12-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_portifolio_user_portifolio"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="portifolio",
        ),
        migrations.AddField(
            model_name="user",
            name="portifolio",
            field=models.ManyToManyField(blank=True, to="core.portifolio"),
        ),
    ]
