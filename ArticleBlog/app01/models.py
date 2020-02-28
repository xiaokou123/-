from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField  #解决富文本不能上传
# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=32,verbose_name='姓名')
    gender = models.CharField(max_length=32,verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    email = models.CharField(max_length=32,verbose_name='邮箱')
    class Meta:
        db_table='author'
        verbose_name_plural="作者"
class Article(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')
    date = models.DateField(auto_now=True,verbose_name='时间日期')
    content = RichTextField(verbose_name='文章内容')
    description = RichTextField(verbose_name="文章描述")
    picture=models.ImageField(upload_to='images',verbose_name='图片')
    recom=models.IntegerField(default=0,verbose_name='推荐')#0是不推荐 1是推荐
    click_l=models.IntegerField(default=0,verbose_name='点击率')
    author=models.ForeignKey(to=author,to_field='id',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table='Article'
        verbose_name_plural='文章表'
class type(models.Model):
    name = models.CharField(max_length=32,verbose_name='类型名字')
    description = models.TextField(verbose_name='描述')
    article=models.ManyToManyField(to=Article)
    class Meta:
        db_table='type'
        verbose_name_plural='文章类型'


class Yonghu(models.Model):
    username=models.CharField(max_length=32,verbose_name='用户名')
    password=models.CharField(max_length=32,verbose_name='密码')
    date=models.DateTimeField(auto_now=True,verbose_name='创建时间')
    class Meta:
        db_table='user'
        verbose_name_plural='用户表'





class publish(models.Model):
    name=models.CharField(max_length=32,verbose_name="出版社名字")
    address=models.CharField(max_length=32,verbose_name="出版社地址")
    class Meta:
        db_table="publish"
        verbose_name_plural="出版社"
class book(models.Model):
    name=models.CharField(max_length=32,verbose_name="书名")
    pub=models.ForeignKey(to=publish,to_field="id",on_delete=models.CASCADE)
    class Meta:
        db_table="book"
        verbose_name_plural="书"
