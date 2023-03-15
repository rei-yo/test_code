from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    class Meta(AbstractUser.Meta):
        db_table    = 'custom_users'

    age = models.IntegerField(verbose_name="年齢",default=20)

# Create your models here.

"""
AbstractUser
username(Unicode)
username,
first_name,
last_name,
email,
is_staff(staff_status)
is_active,
date_joined,

カラム属性のみ追加可能。完全にカスタムする場合はAbstractBaseUserを使用する。
（AbstractBaseUserは認証機能のみ）

"""