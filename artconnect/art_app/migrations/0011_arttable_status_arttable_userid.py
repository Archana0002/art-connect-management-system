# Generated by Django 5.1.6 on 2025-02-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("art_app", "0010_artisttable_userid"),
    ]

    operations = [
        migrations.AddField(
            model_name="arttable",
            name="status",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="arttable",
            name="userid",
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
