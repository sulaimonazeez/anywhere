from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('html', views.basic_html, name="basic_html"),
    path("html/attribute", views.html_attr, name="html_attr"),
    path('html/element', views.html_element, name="html_element"),
    path('html/formatting', views.html_format, name="formatting"),
    path('html/heading', views.html_heading, name="html_heading"),
    path('html/paragraph', views.html_paragraph, name="html_paragraph"),
    path('html/phrase', views.html_phrase, name="phrase"),
    path("html/anchor", views.html_anchor, name="anchor"),
    path("html/image", views.html_image, name="image"),
    path('html/list', views.html_list, name='list'),
    path("html/order", views.html_order, name="order"),
    path("html/unorder", views.html_unorder, name="unorder"),
    path("html/description", views.html_description, name="description"),
    path("html/form", views.html_form, name="form"),
    path("html/input", views.html_input, name="input"),
    path("login", views.login_user, name='login'),
    path("signup", views.sign_up, name='sign'),
    path("logout", views.user_logout, name="logout"),
]