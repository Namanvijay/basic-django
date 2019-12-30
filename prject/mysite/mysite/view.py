from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request,'index.html')

def about(request):

    djname=request.GET.get('naman','default')
    checking=request.GET.get('check','off')
    spaceremov=request.GET.get('spaceremove','off')

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if checking=='on':
        empty=""
        for char in djname:
            if char not in punctuations:
                empty=empty+char
        dict={'purpose':'String without punctuations','new_string':empty}
        return render(request,'second.html',dict)
    elif spaceremov=="on":
        empty=""
        for index,char in enumerate(djname):
            if (djname[index]== " " and djname[index+1]==" "):
                pass
            else:
                empty=empty+char

        dict={'character':empty}
        return render(request,'navigator.html',dict)









