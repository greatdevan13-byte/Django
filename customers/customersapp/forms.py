from django import forms
from .models import customers
class customerform(forms.ModelForm):
    class Meta:
        model= customers
        fields= ['name','email']