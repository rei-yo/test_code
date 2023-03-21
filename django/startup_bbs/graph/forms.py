from django import forms 
from .models import RandomNumber

class RandomNumberForm(forms.ModelForm):

    class Meta:
        model   = RandomNumber
        fields  = ["value"]

