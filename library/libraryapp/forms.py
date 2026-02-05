from django import forms
from .models import library

class libraryForm(forms.ModelForm):
    class Meta:
        model=library
        fields= ['book_title','authors_name']
