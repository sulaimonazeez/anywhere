from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from datetime import datetime
from .forms import myForm
from .models import Contact
from django.http import HttpResponse
def home(request):
  return render(request, 'home.html')
  
def chat(request):
  success = " "
  if request.method == "POST":
    if request.POST['email'] is not None and request.POST['message'] is not None:
      Contact.objects.create(email=request.POST['email'], message=request.POST['message'])
      success += " sent "
      return redirect('/chat')
    else:
      return HttpResponse("you are not proovide email/password")
  form = myForm
  return render(request, 'chat.html', {'form':form, "success":success})
  

def download(request):
  return HttpResponse("error occure while fetching file")
  