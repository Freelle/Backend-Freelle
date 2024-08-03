# Generated by Django 5.0.6 on 2024-08-01 16:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_comentario_favorito"),
        ("uploader", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="uploader.image",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="biografia",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="user",
            name="especializacao",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="instagram",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="isPro",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="linguagem_principal",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="linkedin",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="user",
            name="nacionalidade",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "Brasil"),
                    (2, "Estados Unidos"),
                    (3, "Canadá"),
                    (4, "Reino Unido"),
                    (5, "Alemanha"),
                    (6, "França"),
                    (7, "Japão"),
                    (8, "China"),
                    (9, "Índia"),
                    (10, "Austrália"),
                ],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="username",
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.CreateModel(
            name="Projeto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=80)),
                ("descricao", models.TextField()),
                ("status", models.IntegerField(choices=[(1, "Fechado"), (2, "Em andamento"), (3, "Finalizado")])),
                ("preco", models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ("prazo_entrega", models.DateField()),
                ("data_publicada", models.DateField(default=datetime.datetime.now)),
                ("categoria", models.ManyToManyField(related_name="projetos", to="core.categoria")),
                (
                    "image_project",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="uploader.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Projeto",
                "verbose_name_plural": "Projetos",
            },
        ),
    ]