from django import forms

from django.core.exceptions import ValidationError

def validate_not_gmail(value):
    if value.find('@gmail') != -1:
        raise ValidationError(
            "Gmail is not allowed",
            params={'value': value},)
    
def validate_password(value):
    if len(value)>6:
        raise ValidationError("Password must only contain 6 characters")   
 
class LoginForm(forms.Form):
    email=forms.EmailField(min_length=10, validators=[validate_not_gmail] )
    password=forms.CharField(max_length=10 , validators=[validate_password])