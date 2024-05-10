from django import forms
from .models import Produto, Cliente, Carrinho, Contato


class ProdutosForm(forms.ModelForm):
    class Meta: 
        model = Produto
        fields = "__all__"
        labels = {
            'nome': 'Nome',
            'descricao': 'Descricao',
            'preco': 'Preço',
            'subcategoria' : 'Subcategoria',
                     
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome*', 'required': 'required'})
        self.fields['preco'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Preço*', 'required': 'required'})
        self.fields['descricao'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Descricao*', 'required': 'required'})
        self.fields['subcategoria'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Subcategoria', 'required': 'required'})
        
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = "__all__" 
        labels = {
            'nome': 'Nome',
            'CPF': 'CPF',
            'email': 'Email',
            'telefone': 'Telefone'
            
        }       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome Completo*', 'required': 'required'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control', 'placeholder': 'CPF ou CNPJ*', 'required': 'required'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})          
        self.fields['telefone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Telefone*', 'required': 'required'})    
        

class CarrinhoForm(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = "__all__"
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
            self.fields['cliente'].widget.attrs.update({'class': 'form-select', 'placeholder': 'Usuário*', 'required': 'required'})
            self.fields['cliente'].empty_label = "Usuário*"

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['assunto'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Assunto*', 'required': 'required'})
            self.fields['mensagem'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Mensagem*', 'required': 'required'})
            self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email*', 'required': 'required'})    

