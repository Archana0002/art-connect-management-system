# Generated by Django 5.1.6 on 2025-03-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("art_app", "0017_reviewtable"),
    ]

    operations = [
        migrations.CreateModel(
            name="Carttable",
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
                ("productid", models.IntegerField()),
                ("userid", models.IntegerField()),
                ("status", models.IntegerField()),
            ],
        ),
    ]
