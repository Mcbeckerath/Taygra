from django.shortcuts import render
from TaygraApp.models import Produto
from TaygraApp.forms import  ProdutosForm, ClienteForm, CarrinhoForm, ContatoForm
# Create your views here.

def home (request):
    produtos = Produto.objects.order_by
    context = {'produtos':produtos}
    return render(request, 'base.html', context)

def sobre (request):
    return render(request, 'sobre.html')

def produto (request,id_produto):
    produto = Produto.objects.get(id=id_produto)                                   
    context = {'produto':produto}
    return render(request, 'produto.html', context)

def form_produto(request):
    """Adiciona um novo produto"""
    form = ProdutosForm()
   
    if request.method == 'POST':
            form = ProdutosForm(request.POST)

            if form.is_valid():
                form.save()
                form = ProdutosForm()  

    context = {'form': form}
    return render (request, 'formulario_produto.html', context)

def form_cliente(request):
    """Adiciona um novo produto"""
    form = ClienteForm()
   
    if request.method == 'POST':
            form = ClienteForm(request.POST)

            if form.is_valid():
                form.save()
                form = ClienteForm()  

    context = {'form': form}
    return render (request, 'formulario_cliente.html', context)

def form_contato(request):
    """Adiciona um novo produto"""
    form = ContatoForm()
   
    if request.method == 'POST':
            form = ContatoForm(request.POST)

            if form.is_valid():
                form.save()
                form = ContatoForm()  

    context = {'form': form}
    return render (request, 'formulario_contato.html', context)