from django.db import models
from django.contrib.auth.models import User
class Album(models.Model):
    artist=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    album_name=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return self.artist+'-'+ self.genre












# Create your models here.
