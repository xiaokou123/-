from django.db import models


# Create your models here.
class User(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name='用户名')
    age = models.IntegerField(verbose_name='年龄')
    phone=models.CharField(max_length=11,verbose_name='手机号')
    class Meta:
        db_table = "user"
        verbose_name_plural='用户'