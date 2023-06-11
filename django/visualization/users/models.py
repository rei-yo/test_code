from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils import timezone

from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


class Customer(AbstractBaseUser, PermissionsMixin):

    username_validator  = UnicodeUsernameValidator()
    infra_customer_id          = models.UUIDField( default=uuid.uuid4, primary_key=True, editable=False )
    username    = models.CharField(
                    _('username'),
                    max_length=50,
                    unique=True,
                    help_text=_('最大50文字まで入力できます。記号は@/./+/-/_ のみ使用可能です。'),
                    validators=[username_validator],
                    error_messages={
                        'unique': _("既に存在しているユーザー名です。"),
                    },
                )

    first_name  = models.CharField(_('名前'), max_length=150, blank=True)
    last_name   = models.CharField(_('姓名'), max_length=150, blank=True)

    email       = models.EmailField(_('email address'), blank=True)
    address = models.CharField(verbose_name="住所", max_length=50)
    is_staff    = models.BooleanField(
                    _('staff status'),
                    default=False,
                    help_text=_('adminサイトへのアクセス権限'),
                )

    is_active   = models.BooleanField(
                    _('active'),
                    default=True,
                    help_text=_(
                        'デリートフラグ '
                    ),
                )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    update_time = models.DateTimeField(help_text = "データ更新日")
    create_time = models.DateTimeField(help_text = "データ取得日")
    objects     = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
       

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        if not self.infra_customer_id:
            self.created_time = timezone.now()
        self.update_time = timezone.now()