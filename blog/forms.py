from .models import musicUploader, musicPost
from django import forms

class adminManage(forms.ModelForm):
  class Meta:
    model = musicUploader
    fields = '__all__'
    
class musicPoster(forms.ModelForm):
  class Meta:
    model = musicPost
    fields = ["title", "photo", "file"]
    