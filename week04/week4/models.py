from django.db import models

# Create your models here.
#图书，电影
class Type(models.Model):
    typename = models.CharField(max_length=20)
#作者名字和主演
class Name(models.Model):
    #id (django自动创建)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    stars = models.CharField(max_length=20)
