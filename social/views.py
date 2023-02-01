from django.shortcuts import render, redirect
from .models import Profile
from .forms import Login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
def user_login(request):
  if request.method == "POST":
    x = Login(request.POST)
    if x.is_valid():
      user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('/social')
        else:
          return HttpResponse("disable account")
      else:
        return HttpResponse("username or password is not correct")
    else:
      return HttpResponse("fill out the form")
  form = Login
  return render(request, 'user_login.html', {'form':form})
  
def user_signup(request):
  if request.method == "POST":
    x = Login(request.POST)
    if x.is_valid():
      user = request.POST['username']
      pwd = request.POST['password']
      User.objects.create(username=user, password=request.POST['password'])
      return redirect('login')
    else:
      return HttpResponse('fill out the form')
  form = Login
  
  return render(request, 'user_signup.html', {'form':form})
  
def dashboard(request):
  return render(request, "dashboard.html")
  
def profile_list(request):
  profile = Profile.objects.all()
  return render(request, 'profilelist.html', {'profile':profile})