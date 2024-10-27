from django.contrib import admin
from .models import RetiradaCestaBasica

# Personalização dos títulos do admin
admin.site.site_header = "Paróquia São João Batista"
admin.site.site_title = "Controle de Cestas Básicas"
admin.site.index_title = "Bem-vindo ao Controle de Cestas Básicas da Paróquia"

class RetiradaCestaBasicaAdmin(admin.ModelAdmin):
    # Inclua o método get_beneficiario_nome em list_display
    list_display = ('id_retira', 'get_beneficiario_nome', 'data_retira')
    
    # Permite buscar por nome ou CPF do beneficiário
    search_fields = ('beneficiario__nome', 'beneficiario__cpf')

    # Método para exibir o nome do beneficiário no Django Admin
    def get_beneficiario_nome(self, obj):
        return obj.beneficiario.nome if obj.beneficiario else 'Beneficiário não identificado'
    get_beneficiario_nome.short_description = 'Nome do Beneficiário'

# Registrar o modelo e sua configuração de admin
admin.site.register(RetiradaCestaBasica, RetiradaCestaBasicaAdmin)
