from django.db import models
from django.conf import settings

class UserData(models.Model):

    username  = models.CharField(verbose_name="name",max_length=20)

    def __str__(self):
        return self.username