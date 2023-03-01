from django.db import models


CHOICE = (('danger','high'), ('warning', 'normal'),('primary','low'))


class Category(models.Model):
    name = models.CharField(verbose_name='カテゴリ', max_length=15)
    
    def __str__(self):
        return self.name

class TodoModel(models.Model):
    category = models.ForeignKey(Category, verbose_name = 'カテゴリ', on_delete = models.CASCADE, default = '未分類')
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(max_length=50,
                                choices = CHOICE)
    duedate = models.DateField()
    
    def __str__(self):
        return self.title
    


# Create your models here.
