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

# Create your models here.
