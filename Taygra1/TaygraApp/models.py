from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    CPF_CNPJ = models.CharField(max_length=11)
    email = models.CharField(max_length=250)
    telefone = models.CharField(max_length=20)
    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=250)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE, null=True) 
    def __str__(self):
        return self.cep

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    subcategoria = models.ForeignKey("SubCategoria", on_delete=models.CASCADE)
    def __str__(self):
        return self.nome    
    
class Carrinho(models.Model):
    data = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f"Carrinho de {self.cliente.nome} - {self.data}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"        

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)    
    def __str__(self):
        return self.nome
 
class Pagamento(models.Model):
    carrinho = models.OneToOneField(Carrinho, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=100)
    data = models.DateField()
    def __str__(self):
        return f"Pagamento de {self.total} em {self.data}"

class ListaDesejos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f"Lista de desejos de {self.cliente.nome}"

class ItemListaDesejos(models.Model):
    lista_desejos = models.ForeignKey(ListaDesejos, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.produto.nome} na lista de desejos de {self.lista_desejos.cliente.nome}"
    
class Contato(models.Model):
    assunto = models.CharField(max_length=100)
    mensagem =models.CharField(max_length=200)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.assunto