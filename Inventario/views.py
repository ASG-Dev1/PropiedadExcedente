from django.shortcuts import render

from django.shortcuts import render
from ast import Delete, Not
from audioop import reverse
from .models import Auto, Articulo
from .forms import AutoForm, ArticuloForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.
from django.contrib.auth.decorators import login_required

def excedente(request):
    autos= Auto.objects.order_by('-creado') #for all the records 
    articulos= Articulo.objects.order_by('-creado')
    #one_data = Subasta.objects.get() # 1 will return the first item change it depending on the data you want 
    context={
            'autos':autos,
            'articulos':articulos,
             }
    return render(request, "Excedente.html" , context = context)

@login_required(login_url='login')
def excedenteUploader(request):
    submitted = False
  
    
    if request.method == "POST":
        if (request.POST.get("excedenteButton") == "Auto" ):
            form = AutoForm()
            tipo = "Auto"
        elif (request.POST.get("excedenteButton") == "Articulo" ):
            form = ArticuloForm()
            tipo = "Articulo"
        else:
            form = AutoForm(request.POST, request.FILES)
            form1 = ArticuloForm(request.POST, request.FILES)
            if form.is_valid():
                form = AutoForm(request.POST, request.FILES)
                vin = request.POST['vin']
                usuario = request.user.username
                    
                if Auto.objects.filter(vin__icontains=vin):
                    messages.success(request, "El renglón que desea crear ya existe, intente otro número de subasta.")
                    
                    return HttpResponseRedirect('excedenteuploader?submitted=True')
                if form.is_valid():
                        
                    f = form.save(commit=False)     
                    f.usuario = usuario
                    f.save()
                    messages.success(request, "Se añadió un nueva propiedad excedente.")
                    return HttpResponseRedirect('excedenteuploader?submitted=True')

            
            elif form1.is_valid():
                form = ArticuloForm(request.POST, request.FILES)
                
                usuario = request.user.username
                    
                
                if form.is_valid():
                        
                    f = form.save(commit=False)
                    f.usuario = usuario
                    f.save()
                    messages.success(request, "Se añadió un nueva propiedad excedente.")
                    return HttpResponseRedirect('excedenteuploader?submitted=True')
        
        

    else:
            form = ArticuloForm()
            tipo = "Articulo"
            if 'submitted' in request.GET:
                submitted = True
    

    return render(request, "ExcedenteUploader.html",{'form': form, 'submitted':submitted,'tipo':tipo})

@login_required(login_url='login')
def excedenteAutoDelete(request, vin = None):
    excedente = Auto.objects.get(vin=vin)
    if request.method == 'POST':
        excedente.delete()

        return redirect('/excedente')
    return render (request,'DeleteAuto.html', {'excedente':excedente})

     

@login_required(login_url='login')
def excedenteArticuloDelete(request, articuloid = None):
    excedente = Articulo.objects.get(articuloid=articuloid)
    if request.method == 'POST':
        excedente.delete()

        return redirect('/excedente')
    return render (request,'DeleteAuto.html', {'excedente':excedente})