from django import forms
from .models import Contact

class myForm(forms.Form):
  email = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}))
  message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}))
 

    