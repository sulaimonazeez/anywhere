from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from .forms import adminManage, musicPoster
from .models import musicUploader,  makeConfig, musicPost
from django.http import HttpResponse
def home(request):
  data = makeConfig
  return render(request, 'blog.html', {"data":data})
  
def admin_login(request):
  if request.method == "POST":
    x = adminManage(request.POST, request.FILES)
    if x.is_valid():
      x.save()
      return HttpResponse("saved")
  form = adminManage
  return render(request, 'admin.html', {'form':form})
  
  
def handle_detail(request,  id):
  data = musicUploader.objects.get(id=id)
  return render(request,  'music_detail.html',  {'data':data})
  
def music(request):
  if request.method == "POST":
    fill = request.POST['search']
    data = musicPost.objects.filter(title=fill)
    return render(request, "music.html", {"file":data})
  file = musicPost.objects.all()
  return render(request, "music.html", {'file':file})
def search_music(request):
  data = musicPost.objects.all()
  query = {}
  for api in data:
    query["title"] = str(api.title)
    query["photo"] = "http://127.0.0.1:8000/media/"+str(api.photo)
    query["file"] = "http://127.0.0.1:8000/media/"+str(api.file)
  return JsonResponse(query)
def video(request):
  return render(request, 'video.html')
  
def news(request):
  return render(request, "news.html")
def movie(request):
  return render(request, "movie.html")
  
def album(request):
  return render(request, 'album.html')
  
def post_music(request):
  if request.method == "POST":
    x = musicPoster(request.POST, request.FILES)
    if x.is_valid():
      x.save()
      return HttpResponse("saved")
  form = musicPoster
  data = musicPost.objects.all()
  return render(request, "post_music.html", {"form":form, "data":data})
  
def check(request):
  if request.method == "POST":
    print("get data")
    print(request.POST['search'])
    return HttpResponse("post")
  return HttpResponse("checked")