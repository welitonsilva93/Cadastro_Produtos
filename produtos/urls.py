from django.urls import path
from . import views

urlpatterns = [
    path('fornecedores_lista/', views.fornecedores, name='fornecedores_lista'),
    path('categorias_lista/', views.categorias, name='categorias'),
    path('categoria/<int:categoria_id>/', views.produtos_por_categoria, name='produtos_por_categoria'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('categorias/', views.CategoriasListCreateView.as_view(), name='categorias-list-create'),
    path('categorias/<int:pk>/', views.CategoriasRetrieveUpdateDestroyView.as_view(), name='categorias-detail'),
    path('endereco/', views.EnderecoListCreateView.as_view(), name='endereco-list-create'),
    path('telefone/', views.TelefoneListCreateView.as_view(), name='telefone-list-create'),
    path('fornecedor/', views.FornecedorListCreateView.as_view(), name='fornecedor-list-create'),
    path('fornecedores/<int:pk>/', views.FornecedorRetrieveUpdateDestroyView.as_view(), name='fornecedores-detail'),
    path('produtos/', views.ProdutosListCreateView.as_view(), name='produtos-list-create'),
    path('produtos/<int:pk>/', views.ProdutosRetrieveUpdateDestroyView.as_view(), name='produtos-detail'),
    path('precocusto/', views.PrecoCustoListCreateView.as_view(), name='precocusto-list-create'),
]
