from django.db import models

class musicUploader(models.Model):
  title = models.CharField(max_length=255)
  image = models.ImageField(upload_to='myapp/static')
  music = models.FileField(upload_to='myapp/static')
  class Meta:
    ordering = ('-id', )
  def __str__(self):
    return self.title
    
def makeConfig():
  x = musicUploader.objects.all()
  return x[:15]

class musicPost(models.Model):
  title = models.CharField(max_length=255)
  photo = models.ImageField(upload_to='myapp/static')
  file = models.FileField(upload_to='myapp/static')
  created = models.DateTimeField(auto_now_add=True)
  class Meta:
    ordering = ("-id",)
  def __str__(self):
    return self.title
    