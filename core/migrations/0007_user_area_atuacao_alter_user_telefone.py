# Generated by Django 5.0.6 on 2024-12-15 23:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_user_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="area_atuacao",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="telefone",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Número de telefone inválido.", regex="^\\+?1?\\d{9,15}$"
                    )
                ],
            ),
        ),
    ]
