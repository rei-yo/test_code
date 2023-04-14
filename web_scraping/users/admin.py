from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

#UserAdminはUserクラスを前提としたクラスなので、これを継承してカスタムしていく

class CustomUserAdmin(UserAdmin):

    #fieldsetsはユーザーの詳細画面で表示するフィールド
    #及びユーザーの情報変更を行う際に入力受付を行うフィールドを指定する
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('id',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    #管理サイトからユーザー追加フォームでユーザーから入力を受け付けるフィールドを指定
    add_fieldsets = (
        (None, {
            'classes': ('wide',), # wide??
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    
# https://daeudaeu.com/django-useradmin/#i

    #ユーザー一覧リストに表示するフィールドを指定するクラス変数
    list_display = ['username']
    #ユーザー検索時に検索対象に含めるフィールドを指定
    search_fields = ['username']
    
    list_filter = ( "is_superuser", "groups")


#管理画面で使用するクラスを第二引数で指定、CustomUserAdminが利用できるように
#第一引数は指定したモデルのインスタンスを管理する
#以下の場合、CustomUserAdminで作成される管理画面でCustomUserのインスタンスを管理する
admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
