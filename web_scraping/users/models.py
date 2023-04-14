from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

#多言語対応（翻訳）
from django.utils.translation import gettext_lazy as _
# from django.core.mail import send_mail

import uuid



#AbstractBaseUser：一般的なユーザー情報管理（username,emailなど）
#PermissionsMixin（グループ権限管理、is_superuser,groupなど)
#AbstractUserだとlastnameなども含まれるのでより自由度高くカスタマイズしたければこちらを使用する
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username_validator  = UnicodeUsernameValidator()
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username    = models.CharField(
                _('username'),
                max_length=150,
                unique=True,
                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                validators=[username_validator],
                error_messages={
                    'unique': _("A user with that username already exists."),
                },
            )
    
    USERNAME_FIELD = 'username' #??

# Create your models here.
