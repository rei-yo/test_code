from django.db import models

class Category(models.Model):

    name    = models.CharField(verbose_name="カテゴリ名",max_length=20)

    def __str__(self):
        return self.name


class Topic(models.Model):
    category    = models.ForeignKey(Category,verbose_name="カテゴリ",on_delete=models.CASCADE, default = '未分類')
    comment     = models.CharField(verbose_name="コメント",max_length=50)

    def __str__(self):
        return self.comment


class Album(models.Model):

    photo       = models.ImageField(verbose_name="フォト",upload_to="bbs/album/photo/", null=True,blank=True)

class Document(models.Model):

    file        = models.FileField(verbose_name="ファイル",upload_to="bbs/document/file/", null=True,blank=True)
# Create your models here.
