from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('login', views.admin_login, name='login'),
  path("music/<int:id>",  views.handle_detail, name='music_detail'), 
  path("music", views.music, name='music'),
  path("video", views.video, name='video'),
  path("news", views.news, name='news'),
  path("movie", views.movie, name='movie'),
  path("album", views.album, name='album'),
  path("fake", views.post_music, name="post_music"),
  path("check", views.check, name='check'),
  path("search", views.search_music, name="search_music"),
]