from django.db import models
from django.conf import settings

class Category(models.Model):

    name    = models.CharField(verbose_name="カテゴリ名",max_length=20)

    def __str__(self):
        return self.name


class User(models.Model):
    
    name = models.CharField(verbose_name = 'user_class', max_length = 20)
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    category    = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE, default = 1)
    user_name    = models.ManyToManyField(User , verbose_name = 'ユーザー名', blank = True)
    comment     = models.CharField(verbose_name="コメント",max_length=50)
    #DBに格納されるのは文字列型。
    photo       = models.ImageField(verbose_name="フォト",upload_to="bbs/topic/photo/", null=True,blank=True)
    
    # ここに誰が投稿したか、CustomUserと1対多で紐づくようにフィールドを追加しておく
    user    = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="ユーザー",on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Album(models.Model):

    photo = models.ImageField(verbose_name="フォト",upload_to="bbs/album/photo/", null=True,blank=True)

class Document(models.Model):

    file    = models.FileField(verbose_name="ファイル",upload_to="bbs/document/file/", null=True,blank=True)
# Create your models here.
