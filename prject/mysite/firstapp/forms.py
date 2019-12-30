from django import forms
from .import models

class createalbum(forms.ModelForm):
    class Meta:
        model=models.Album
        fields=['artist','genre','album_name',]


