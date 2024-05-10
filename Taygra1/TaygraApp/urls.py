from django.urls import path
from TaygraApp import views


urlpatterns = [
   
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('delusuario/<id>', views.delusuario, name='delusuario'),
    
]