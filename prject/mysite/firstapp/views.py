from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Album
from django.contrib.auth.decorators import login_required
from .import forms
from django.contrib.auth.models import User



def index(request):
    album=Album.objects.all().order_by('date')
    dict={'albums':album}


    return render(request,'firstapp/index.html',dict)
def fun1(request,album_genre):
     album=Album.objects.get(genre=album_genre)
     dict={'album':album}
     return render(request,'firstapp/index2.html',dict)
@login_required(login_url='/account/login/')
def create(request):


    if request.method=='POST':
        form=forms.createalbum(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('firstapp:index')
    else:
            form=forms.createalbum()

    return render(request,'firstapp/create.html',{'form':form})












# Create your views here.
