from .views import (UsuariosView, AddUsuario,EditarUsuario,EliminarUsuario,DetailUsuario,
                     AddUsuario2)

from django.urls import path


app_name = 'Usuarios'
urlpatterns = [

    path('', UsuariosView, name='usuario'),
    path('AddUsuario', AddUsuario, name='addusuario'),
    path('AddUsuario2/<str:token>/',
         AddUsuario2, name='addusuario2'),

    path('eliminarusuario/<usuario_id>',
         EliminarUsuario, name='eliminarusuario'),
    path('editarusuario/<usuario_id>', EditarUsuario, name='editarusuario'),
    path('detailsusuario/<usuario_id>/', DetailUsuario, name='detailsusuario'),
]