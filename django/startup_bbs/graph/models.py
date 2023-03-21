from django.db import models

class RandomNumber(models.Model):
    #integerFieldに複数の値を格納できる？
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
# Create your models here.
