# Generated by Django 5.1.6 on 2025-02-13 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('art_app', '0002_artisttable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artisttable',
            name='photo',
        ),
    ]
