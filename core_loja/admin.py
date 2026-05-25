from django.contrib import admin
from .models import Empresa, Produto, Cliente

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ramo')

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'empresa')
    list_filter = ('empresa',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Exibe as informações principais do cliente em colunas na tabela
    list_display = ('nome', 'cpf', 'email', 'telefone', 'cidade', 'empresa', 'ativo')
    
    # Adiciona filtros na lateral direita para facilitar a busca
    list_filter = ('ativo', 'empresa', 'cidade')
    
    # Cria uma barra de pesquisa para buscar por nome ou CPF
    search_fields = ('nome', 'cpf')
