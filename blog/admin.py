from django.contrib import admin
from .models import musicUploader, musicPost

admin.site.register(musicPost)
admin.site.register(musicUploader)
