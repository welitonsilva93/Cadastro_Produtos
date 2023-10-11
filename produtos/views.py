from django.shortcuts import render
from .serializers import (
    CategoriasSerializer,
    EnderecoSerializer,
    TelefoneSerializer,
    FornecedorSerializer,
    ProdutosSerializer,
    PrecoCustoSerializer,
)
from rest_framework import generics
from .models import Categorias, Endereco, Fornecedor, Telefone, Produtos, PrecoCusto

#Lugar das Categorias separadin
class CategoriasListCreateView(generics.ListCreateAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer

class CategoriasRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorias.objects.all()
    serializer_class = CategoriasSerializer


#Lugar dos Endereços separadin
class EnderecoListCreateView(generics.ListCreateAPIView):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class TelefoneListCreateView(generics.ListCreateAPIView):
    queryset = Telefone.objects.all()
    serializer_class = TelefoneSerializer

#Os Fornecedores separadin
class FornecedorListCreateView(generics.ListCreateAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

class FornecedorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


#Aqui São os Produtos pra ficar separadin também
class ProdutosListCreateView(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer

class ProdutosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


class PrecoCustoListCreateView(generics.ListCreateAPIView):
    queryset = PrecoCusto.objects.all()
    serializer_class = PrecoCustoSerializer

def categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})

def produtos_por_categoria(request, categoria_id):
    categoria = Categorias.objects.get(pk=categoria_id)
    produtos = Produtos.objects.filter(categoria=categoria)
    return render(request, 'produtos_por_categoria.html', {'categoria': categoria, 'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = Produtos.objects.get(pk=produto_id)
    precos = PrecoCusto.objects.filter(produto=produto)
    return render(request, 'detalhes_produto.html', {'produto': produto, 'precos': precos})

def fornecedores(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'fornecedores.html', {'fornecedores': fornecedores})