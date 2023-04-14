from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# UserCreationFormは類似したユーザー名との混同を防ぐため、大文字小文字のみが異なるユーザー名も非許可
class SignupForm(UserCreationForm):
    
    # UserCreationForm.Meta??メタを継承？
    class Meta(UserCreationForm.Meta):
        model   = CustomUser
        fields  = ("username")