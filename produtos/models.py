from django.db import models


class Categorias(models.Model):
    nome_categoria = models.CharField(max_length=200, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.nome_categoria


class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=20)
    complemento = models.CharField(max_length=200, blank=True, null=True)
    cep = models.CharField(max_length=10)
    cidade = models.CharField(max_length=75)
    estado = models.CharField(max_length=45)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}, {self.estado}'


    
class Fornecedor(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    telefones = models.ManyToManyField('Telefone')

    def __str__ (self):
        return self.nome_fantasia


class Telefone(models.Model):
    TIPOS_TELEFONE = (
        ('celular', 'Celular'),
        ('fixo', 'Fixo'),
        ('comercial', 'Comercial'),
    )
    tipo = models.CharField(max_length=20, choices=TIPOS_TELEFONE)
    numero = models.CharField(max_length=20, unique=True)


    def __str__(self):
        return f'{self.tipo}: {self.numero}'


  
class Produtos(models.Model):
    nome_produto = models.CharField(max_length=200, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fornecedores = models.ManyToManyField(Fornecedor, through='PrecoCusto')

    def __str__(self):
        return self.nome_produto



class PrecoCusto(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'{self.fornecedor} - {self.produto} - R${self.preco_custo}'
