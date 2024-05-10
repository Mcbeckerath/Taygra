from django.contrib import admin
from TaygraApp.models import Cliente, Endereco, Carrinho, ItemCarrinho, Produto, SubCategoria,Categoria, ListaDesejos, ItemListaDesejos, Pagamento

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(Carrinho)
admin.site.register(ItemCarrinho)
admin.site.register(Produto)
admin.site.register(SubCategoria)
admin.site.register(Categoria)
admin.site.register(ListaDesejos)
admin.site.register(ItemListaDesejos)
admin.site.register(Pagamento)

# Register your models here.
