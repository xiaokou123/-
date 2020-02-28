from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Article)
admin.site.register(type)
admin.site.register(author)
admin.site.register(publish)
admin.site.register(book)
admin.site.register(Yonghu)
