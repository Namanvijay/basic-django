
from django.conf.urls import include
from django.urls import path
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views
app_name='firstapp'

urlpatterns = [

    path('', views.index, name="index"),
    url(r'^create/$',views.create,name="create"),


    url(r'^(?P<album_genre>[\w-]+)/$',views.fun1,name="fun1"),








]



