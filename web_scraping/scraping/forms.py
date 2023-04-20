from django import forms 
from .models import GoodCompany

class GoodCompanyForm(forms.ModelForm):

    class Meta:
        model   = GoodCompany
        fields  = ["company_info", "user", "ip"]