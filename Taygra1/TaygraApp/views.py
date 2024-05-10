from django.shortcuts import render
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from TaygraApp.forms import UsuarioForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Create your views here.
def home (request):
     loginform = LoginForm()
     usuarioform = UsuarioForm()
     context = {'loginform': loginform, 'usuarioform': usuarioform}
     return render(request, 'base.html', context)
     
    

def login (request):
    if request.method == "POST":
        #fazer login
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            auth_login(request, user = user)
    return HttpResponseRedirect(reverse('home'))

def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def cadastro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password') != form.data.get('confirmacao'):
                form.add_error('password', 'As senhas devem ser iguais')
            else:
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data.get('password'))
                user.save()
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UsuarioForm()

    context = {'usuarioform': form}
    return render(request, 'index.html', context)

def delusuario (request, id):
    user = User.objects.get(id=id)
    user.delete()
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))

def editar_perfil (request):
    if request.method == 'POST':
        usuario = User.objects.get(id=request.user.id)
        novo_usuario = request.POST.copy()
        novo_usuario['username'] = usuario.username
        novo_usuario['password'] = usuario.password
        user = UsuarioForm(instance=usuario, data=novo_usuario)
        if user.is_valid:
            user.save()
    return HttpResponseRedirect(reverse('home'))
