from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
iter=(('1','Male'),('2','Female'),('3','Other'))


class Userregistrationform(UserCreationForm):
    email=forms.EmailField()
    gender=forms.ChoiceField(choices=iter)
    first_name=forms.CharField()
    last_name=forms.CharField()
    mobile=forms.CharField(max_length=12)
    birth=forms.DateField(label='Enter your birth date',
    widget=forms.SelectDateWidget)



    class Meta:
        model=User
        fields=['username','email','password1','password2','last_name','first_name','gender','mobile','birth']

