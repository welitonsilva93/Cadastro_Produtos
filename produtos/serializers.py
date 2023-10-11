from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import *
from validate_docbr import CNPJ


class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = '__all__'
    
    def validate_nome_produto(self, value):
        if Produtos.objects.filter(nome_produto=value).exists():
            raise serializers.ValidationError("Este produto já existe.")
        return value



class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

    def validate_nome_categoria(self, value):
        if Categorias.objects.filter(nome_categoria=value).exists():
            raise serializers.ValidationError("Esta categoria já existe.")
        return value



class EnderecoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Endereco
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'

    def validate_cnpj(self, cnpj):
        
        cnpj = ''.join(filter(str.isdigit, cnpj))

        
        if CNPJ().validate(cnpj):
            return cnpj
        else:
            raise serializers.ValidationError("CNPJ inválido.")


class PrecoCustoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrecoCusto
        fields = '__all__'


