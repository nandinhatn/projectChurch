from django.contrib import admin

# Register your models here.
from .models import Beneficiario

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf','endereco', 'qtd_membros_familia', 'data_cadastro', 'data_nascimento')
    search_fields = ('nome',)
    list_filter = ('data_cadastro', 'qtd_membros_familia')