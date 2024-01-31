from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from Inventario .models import Articulo, Auto
# Create your views here.

def login(request):
    
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)

       if user is not None:
           auth.login(request, user)
           return redirect('/indice')
       else:
           messages.info(request, 'Credenciales Invalidos Comunicarse con ODI')
           return redirect('login')

   else:
       return render(request, 'login.html')
   


@login_required(login_url='login')
def indice(request):

    auto= Auto.objects.all()
    articulo= Articulo.objects.all()
    context = {
        'autos': auto,
        'articulos': articulo,
    }

    return render(request, 'prodis/index.html', context)

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('/')