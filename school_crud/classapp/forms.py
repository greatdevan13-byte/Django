from django import forms
from .models import School

class Studentform(forms.ModelForm):
    class Meta:
        model= School
        fields= ['name', 'student_class' ,'age']