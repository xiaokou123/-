# Generated by Django 2.2.1 on 2020-02-18 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_auto_20200218_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
    ]
