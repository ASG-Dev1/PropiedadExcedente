from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm


class UsuarioFormParte1(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'puesto', 'nombre', 'extension', 'Rol', 'email','vigencia')
        labels = {

            'username': 'Nombre de usuario',
            'puesto': 'Puesto',
            'nombre': 'Nombre',
            'extension': 'Extension',
            'Rol': 'Rol:',
            'email': 'Correo electrónico',
            'vigencia':'vigencia',
            
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte nombre de usuario.', 'style': 'margin-top:10px'}),
            'puesto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte descripción de subasta.', 'style': 'margin-top:10px'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inserte número de subasta.', 'width': '10px', 'style': 'margin-top:10px'}),
            'extension': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escoja tipo de subasta.', 'style': 'margin-top:10px'}),
            'Rol': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Inserte agencia.', 'style': 'margin-top:10px'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Inserte propósito.', 'style': 'margin-top:10px'}),
            'vigencia': forms.SelectDateWidget(years=range(2015, 2030), attrs={'class': 'form-control', 'placeholder': 'Escoja una fecha', 'style': 'margin-top:10px'}),


        }

class UsuarioFormParte2(forms.ModelForm):
    confirm_email = forms.EmailField(
        label='Confirmar correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Inserte correo electrónico.', 'style': 'margin-top:10px'})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Inserte contraseña.', 'style': 'margin-top:10px'})
    )
    confirm_password = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme contraseña.', 'style': 'margin-top:10px'})
    )

    class Meta:
        model = Usuario
        fields = ('confirm_email', 'password')
        labels = {
            'password': 'Contraseña'
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Inserte contraseña.', 'style': 'margin-top:10px'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = self.instance.email  # Obtener el correo electrónico del Usuario 1
        confirm_email = cleaned_data.get('confirm_email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if confirm_email and confirm_email != email:
            self.add_error('confirm_email', "El correo electrónico no coincide con el ingresado por el Administrador.")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "La contraseña no coincide.")

        return cleaned_data


class CorreoDestinoForm(forms.Form):
    correo_destino = forms.EmailField(
        label='Correo electrónico de destino', max_length=100)
