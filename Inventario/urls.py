from django.urls import path
from .forms import AutoForm, ArticuloForm
from .views import excedente , excedenteUploader, excedenteAutoDelete, excedenteArticuloDelete


app_name = 'excedente'
urlpatterns = [
    path('', excedente, name="excedente"),
    path('uploader', excedenteUploader, name="excedenteUploader"),
    path('autodelete/<slug:vin>', excedenteAutoDelete, name='excedenteautodelete'),
    path('articulodelete/<slug:articuloid>', excedenteArticuloDelete, name='excedentearticulodelete'),
  
    
]
