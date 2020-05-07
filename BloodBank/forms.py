from django.contrib.auth.models import BloodBank
from django import forms
from myuser.models import Myuser

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Myuser
        fields=['email','password','organisation_name','user_type']

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Myuser
        fields=['email','password','user_type']