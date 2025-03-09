# Generated by Django 5.1.6 on 2025-03-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("art_app", "0016_remove_ordertable_payment_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="reviewtable",
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
                ("userid", models.CharField(max_length=30)),
                ("product_id", models.CharField(max_length=30)),
                ("rev_title", models.CharField(max_length=30)),
                ("rev_body", models.CharField(max_length=30)),
                ("rating", models.CharField(max_length=30)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
