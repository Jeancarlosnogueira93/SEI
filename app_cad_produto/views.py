from django.shortcuts import render
from .models import Produtos

def home(request):
    return render(request,'produtos/produtos.html')

def produto(request):
    #SALVAR OS DADOS PARA BANCO DE DADOS
    novo_produto = Produtos()
    novo_produto.codigo = request.POST.get('codigo')
    novo_produto.descricao = request.POST.get('descricao')
    novo_produto.quantidade = request.POST.get('quantidade')
    novo_produto.save()
    #Exibir dados do banco de dados
    produtos_novo = {
        'produtos_novo' : Produtos.objects.all()   
    }
    #Listar os dados
    return render(request,'produtos/historico.html',produtos_novo)
    
   