from django.urls import path
from . import views
urlpatterns = [
  path('login', views.user_login, name='login'),
  path('signup', views.user_signup, name='signup'),
  path('', views.dashboard, name="dashboard"),
  path("profilelist", views.profile_list, name="profile_list"),
]