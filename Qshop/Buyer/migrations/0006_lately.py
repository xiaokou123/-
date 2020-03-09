# Generated by Django 2.2.1 on 2020-03-07 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0009_auto_20200304_2108'),
        ('Buyer', '0005_shaddress_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lately',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.Goods')),
            ],
            options={
                'db_table': 'lately',
                'verbose_name_plural': '最近浏览表',
            },
        ),
    ]