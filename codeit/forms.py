from django import forms
from django.contrib.auth.models import User
class Login(forms.ModelForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', "placeholder":"Username"}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', "placeholder":"Password"}))
  class Meta:
    model = User
    fields = ["username", "password"]
    
    widgets = {
         "username": forms.TextInput(attrs={'class':'form-control'})
      }
