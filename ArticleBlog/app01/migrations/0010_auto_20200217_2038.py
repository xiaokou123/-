# Generated by Django 2.2.1 on 2020-02-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20200217_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='时间日期'),
        ),
    ]
