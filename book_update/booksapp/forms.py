from django import forms
from .models import Books

class booksform(forms.ModelForm):
    class Meta:
        model =Books
        fields=["title","author",'year']