from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils import timezone
from django.utils.timezone import now
import uuid




# HINT: BUSQUEN EN SETTINGS.PY LA CONFIGURACIÓN Y BUSQUEN INFORMACIÓN DE ELLA 
# TO DO: EN LANDING EN LA FUNCIÓN LOGIN EDITAR EL CODIGO PARA QUE NO PUEDA ENTRAR SI NO TIENE FECHA VIGENCIA ACTIVO.
# WARNING: LA FUNCIÓN LOGIN ACTUALMENTE VALIDA SI TIENES CUENTA CUANDO HAGAN EL CODIGO DE FECHA VIGENCIA MANTENGAN ESA VALIDACIÓN ACTIVA.
# TO DO: EN class Usuario DEBEN AGREGAR UN CAMPO BOOL PARA QUE MARQUE SI EL USUARIO SE ENCUENTRA DENTRO DE FECHA VIGENCIA 
# PUEDE ACCEDER AL PORTAL, SINO NO PODRÁ ACCEDER A ÉL.
# HINT: EN CADA VISTA VALIDEN QUE EL USUARIO ESTE DENTRO DE FECHA VIGENCIA, NO SOLO EN LANDING

tipo_ref = (('ASG', 'ASG'),
            ('IT', 'Tecnico'), ('Externo', 'Externo'))


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    
    usuario_id = models.CharField(
        max_length=200, unique=True, default=uuid.uuid4)
    puesto = models.CharField(max_length=30, blank=False)
    nombre = models.CharField(max_length=60, blank=False)
    extension = models.CharField(max_length=60, blank=False)
    Rol = models.CharField(max_length=30, choices=tipo_ref,
                           default=('', ''), blank=False)
   
    password = models.CharField(max_length=255, blank=False)
    vigencia = models.DateField(blank=True, null=True)
    activo = models.BooleanField(null=True,blank=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','first_name', 'last_name']
    def save(self, *args, **kwargs):
        if self.pk is not None:  # Check if the instance already exists in the database
            original_instance = self.__class__.objects.get(pk=self.pk)  # Get the original instance from the database
            if self.password != original_instance.password:  # Compare the current password with the original password
                password_changed = True
            else:
                password_changed = False
        else:
            password_changed = True  # New instance, so password is considered changed
        
        if password_changed:
            self.set_password(self.password)
            print("Password has changed")
            # Your password change logic here

        if self.Rol == 'ASG':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
                # Si vigencia es None, se asume que no hay restricción de tiempo (podrías ajustar esto según tu lógica de negocio)
        if self.vigencia is not None:
            self.activo = now().date() <= self.vigencia
        else:
            self.activo = True  # o False, según lo que desees por defecto cuando no hay fecha de vigencia
            super().save(*args, **kwargs)

        super().save(*args, **kwargs)




def __str__(self):
    return str(self.agencia.nombre)
    
def generate_token():
        return str(uuid.uuid4())
class Invitation(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    invited_by = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def is_valid(self):
        return timezone.now() <= self.expiration_date
