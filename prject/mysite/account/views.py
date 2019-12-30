from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User,auth
from .forms import Userregistrationform

def signup(request):
    if request.method=='POST':

        form=Userregistrationform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('firstapp:index')


    else:
         form=Userregistrationform()
         dict={'form':form}

    return render(request, 'account/index.html',dict)





def login_in(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('firstapp:index')
    else:
        form=AuthenticationForm()
    dict={'form':form}
    return render(request,'account/login.html',dict)
def logout_out(request):
    if request.method=='POST':
        logout(request)
        return redirect('firstapp:index')






