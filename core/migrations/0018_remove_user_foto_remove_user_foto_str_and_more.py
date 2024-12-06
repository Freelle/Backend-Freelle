# Generated by Django 5.0.6 on 2024-12-06 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_alter_user_foto"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="foto",
        ),
        migrations.RemoveField(
            model_name="user",
            name="foto_str",
        ),
        migrations.AddField(
            model_name="user",
            name="total_pedidos",
            field=models.FloatField(default=0),
        ),
    ]