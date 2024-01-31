from django.contrib import admin
from django.urls import  path
from .views import (login,indice,logout)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', login, name="login"),
    path('login', login, name="login"),
    path('indice', indice, name="indice"),
    path('logout', logout, name='logout'),



] 