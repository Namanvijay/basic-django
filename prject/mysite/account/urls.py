from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from django.conf.urls import url

app_name='account'

from .import views

urlpatterns = [
    url(r'^signup/$',views.signup,name="signup"),
    url(r'^login/$',views.login_in,name="login"),
    url(r'^logout/$',views.logout_out,name="logout"),



]