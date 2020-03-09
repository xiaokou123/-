# Generated by Django 2.2.1 on 2020-03-02 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0007_auto_20200227_1126'),
        ('Buyer', '0002_auto_20200227_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_number', models.IntegerField(verbose_name='商品的数量')),
                ('goods_total', models.FloatField(verbose_name='商品的小计')),
                ('cart_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.LoginUser', verbose_name='买家')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seller.Goods')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
