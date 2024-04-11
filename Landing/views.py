from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.shortcuts import redirect
from django.contrib import messages
from Usuarios .models import Usuario
from django.utils.timezone import now
from Inventario .models import Articulo, Auto
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # Comprobar la vigencia del perfil de usuario
            try:
                usuarios = Usuario.objects.get(first_name=user.first_name)
                if usuarios.vigencia and usuarios.vigencia < now().date():
                    # Si la vigencia ha expirado, mostrar mensaje de error y no iniciar sesión
                    messages.info(request, 'La cuenta ha expirado. Comuníquese con ODI.')
                    return redirect('login')
            except Usuario.DoesNotExist:
                # Manejar el caso en que el usuario no tenga un perfil asociado si es necesario
                pass

            # Si todo está en orden, proceder con el inicio de sesión
            auth.login(request, user)
            return redirect('/indice')
        else:
            messages.info(request, 'Credenciales inválidos. Comuníquese con ODI.')
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