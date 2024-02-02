from django.shortcuts import render
from .models import Usuario, Invitation, generate_token
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import UsuarioFormParte1,UsuarioFormParte2
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.shortcuts import redirect

# Create your views here.

Usuarios = []
# OBSERVEN LOS MODELOS PRIMERO, LUEGO FORMS, LUEGO VIEWS,  Y AL FINAL LA URLS
# 1) Al crear un usuario llamamos al form para que cargue los campos
# 2) Una vez se introduce la información valida los campos y envia por email el generate_token HINT: observa los modelos en Usuario
# para poder identificar el campo token. También observa los setting.py en PropiedadExcedente para la configuración del email.
# WARNING: Al momento tirará un error, o no llegará el email. OBSERVA LOS SETTINGS.PY. 
# 4)Pasa a la función AddUsuario2.


def AddUsuario(request):
    submitted = False

    if request.method == "POST":
        form = UsuarioFormParte1(request.POST, request.FILES)

        if form.is_valid():
            usuario_data = form.cleaned_data
            

            usuario = Usuario(**usuario_data)
            usuario.save()


            

            expiration_date = timezone.now() + timezone.timedelta(days=7)
            token = generate_token()
            invitation = Invitation(email=usuario.email, token=token, expiration_date=expiration_date, invited_by=request.user)
            invitation.save()

            # Asignar el token al usuario
            usuario.fecha_de_invitacion = timezone.now() 
            usuario.token = token
            usuario.save()

            # Generar el enlace de invitación con el token del usuario
            addusuario2_url = request.build_absolute_uri(f'/usuariosAddUsuario2/{token}')

            user_requesting_email = render_to_string('Usuarios/email_message.html', {
                'name': usuario.nombre,
                'username': usuario.username,
                'addusuario2_url': addusuario2_url,
            })

            subject = 'Invitación para completar el formulario'

            user_email = usuario.email

            # Dirección de correo electrónico a la que deseas enviar una copia
            cc_email = ['mrmerced@asg.pr.gov']

            # Renderizar el mensaje HTML para la copia con información específica
            copy_email_html = render_to_string('Usuarios/copy_email_message.html', {
                'name': usuario.nombre,
                'email': usuario.email,
                'username': usuario.username,
                'invitation_time': usuario.fecha_de_invitacion.strftime("%Y-%m-%d %H:%M:%S"),
            })

            # Enviar el correo electrónico principal al usuario
            send_mail(
                subject,
                '',
                'noreply@asg.pr.gov',
                [user_email],
                html_message=user_requesting_email,
                fail_silently=False,
            )

            # Enviar una copia del correo electrónico con información específica
            send_mail(
                'Copia del correo de invitación',
                '',
                'noreply@asg.pr.gov',
                cc_email,
                html_message=copy_email_html,
                fail_silently=False,
            )

            messages.success(request, "Se añadió un nuevo usuario.")
            redirect_url = '/usuariosAddUsuario?submitted=True'

            return HttpResponseRedirect(redirect_url)
    else:
        form = UsuarioFormParte1()

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Usuarios/AddUsuario.html', {'form': form, 'submitted': submitted})


# 1) El token que se envió lo recibe esta función y de ahí el usuario debe marcar su email.
# Si su email no es el mismo que esta ya registrando en el UsuarioForm1, no es valido.
# 2) La función llama al UsuarioForm2 para obtener los passwords y validar que sean el mismo.


def AddUsuario2(request, token):
    submitted = False

    # Obtener la instancia del usuario existente
    invitation_token = token

    try:
        invitation = Invitation.objects.get(token=invitation_token)
        usuario = get_object_or_404(Usuario, email=invitation.email)
        if invitation.is_valid():
            if request.method == 'POST':
                form = UsuarioFormParte2(request.POST, instance=usuario)

                if form.is_valid():
                    # Verifica si el formulario es válido antes de continuar
                    email_usuario1 = usuario.email
                    email_usuario2 = form.cleaned_data.get('confirm_email')

                    # Verificar si el correo electrónico del Usuario 2 coincide con el del Usuario 1
                    if email_usuario2 != email_usuario1:
                        form.add_error('confirm_email', "El correo electrónico no coincide con el ingresado por el Administrador.")
                    else:
                        # Aquí puedes verificar si el formulario es válido
                        # antes de guardar la contraseña
                        if form.cleaned_data.get('password') == form.cleaned_data.get('confirm_password'):
                            form.save()
                            messages.success(request, "Se actualizó el usuario.")
                            redirect_url = f'/usuariosAddUsuario2/{token}?submitted=True'
                            return HttpResponseRedirect(redirect_url)
                        else:
                            form.add_error('confirm_password', "Las contraseñas no coinciden.")

            else:
                form = UsuarioFormParte2(instance=usuario)

            submitted = 'submitted' in request.GET

            return render(request, 'Usuarios/AddUsuario2.html', {'form': form, 'submitted': submitted})

    except:
        raise



def access_denied(request):
    raise Http404("Access denied")



# 1) Llama a todos los usuarios para mostrarlo.
# 2) Tiene una función que conecta con el search de navbar. HINT: TIENE UN PEQUEÑO "BUG"

@login_required
def UsuariosView(request):
    usuarios = Usuario.objects.order_by('nombre')
    if request.method == "POST":

        if (request.POST.get("search") != None):
            search = request.POST.get("search")
        if request.user.is_staff:

            usuarios = (Usuario.objects.filter(username__icontains=search)) or (
                Usuario.objects.filter(nombre__icontains=search))

            context = {'usuarios': usuarios}
            return render(request, 'Usuarios/Usuarios.html', context)

    context = {'usuarios': usuarios}

    return render(request, 'Usuarios/Usuarios.html', context)



@login_required
def EditarUsuario(request, usuario_id=None):
    submitted = False
    usuario = Usuario.objects.get(usuario_id=usuario_id)

    if request.method == "POST":
        form = UsuarioFormParte1(request.POST, instance=usuario)

        if form.is_valid():
            # Actualizar solo los campos específicos del usuario
            usuario.puesto = form.cleaned_data['puesto']
            usuario.nombre = form.cleaned_data['nombre']
            usuario.extension = form.cleaned_data['extension']
            usuario.Rol = form.cleaned_data['Rol']
            
            vigencia_day = request.POST.get('vigencia_day')
            vigencia_month = request.POST.get('vigencia_month')
            vigencia_year = request.POST.get('vigencia_year')
            
            usuario.vigencia = usuario.vigencia.replace(day=int(
            vigencia_day), month=int(vigencia_month), year=int(vigencia_year))

            usuario.save()

            message = ('El usuario se editó')
            messages.success(request, message)
            submitted = True
            return render(request, 'Usuarios/UsuariosEdit.html', {'usuario': usuario, 'submitted': submitted})

    else:
        form = UsuarioFormParte1(instance=usuario)

    return render(request, 'Usuarios/UsuariosEdit.html', {'form': form, 'usuario': usuario, 'submitted': submitted})


@login_required
def EliminarUsuario(request, usuario_id=None):

    usuario = Usuario.objects.get(usuario_id=usuario_id)
    if request.method == 'POST':

        usuario.delete()

        return redirect('/usuarios')

    return render(request, 'Usuarios/UsuariosDelete.html', {'usuario': usuario})


@login_required
def DetailUsuario(request, usuario_id=None):

    usuario = Usuario.objects.get(usuario_id=usuario_id)

    return render(request, 'Usuarios/DetailsUsuario.html', {'usuario': usuario})

