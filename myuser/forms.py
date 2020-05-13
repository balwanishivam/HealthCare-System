from django.contrib.auth.models import User
from django import forms
from .models import Myuser

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Myuser
        fields=['email','password','password2','user_type']

class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Myuser
        fields=['email','password']