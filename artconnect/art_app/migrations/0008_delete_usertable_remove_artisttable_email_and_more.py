# Generated by Django 5.1.6 on 2025-02-26 07:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("art_app", "0007_arttable"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Usertable",
        ),
        migrations.RemoveField(
            model_name="artisttable",
            name="email",
        ),
        migrations.RemoveField(
            model_name="artisttable",
            name="name",
        ),
    ]
