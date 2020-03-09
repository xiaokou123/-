# Generated by Django 2.2.1 on 2020-03-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0008_validcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='validcode',
            name='email',
        ),
        migrations.AddField(
            model_name='validcode',
            name='phone',
            field=models.CharField(default=1, max_length=32, verbose_name='手机号'),
            preserve_default=False,
        ),
    ]
