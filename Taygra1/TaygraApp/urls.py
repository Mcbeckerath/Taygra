from django.urls import path
from TaygraApp import views


urlpatterns = [
   
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('produto/<id_produto>', views.produto, name='produto'),
    path('form_produto/', views.form_produto, name ='form_produto'),
    path('form_cliente/', views.form_cliente, name='form_cliente'),
    path('form_contato/', views.form_contato, name= 'form_contato')
]