# Generated by Django 5.0.6 on 2024-12-17 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_alter_userprojeto_empresa_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nacionalidade",
            name="cidade",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]