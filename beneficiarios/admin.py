from django.contrib import admin
from .models import Beneficiario
from retiradas_cestas_basicas.models import RetiradaCestaBasica

class RetiradaCestaBasicaInline(admin.TabularInline):
    model = RetiradaCestaBasica
    extra = 0
    readonly_fields = ('beneficiario',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('beneficiario')

class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'endereco', 'qtd_membros_familia', 'data_cadastro', 'data_nascimento')
    inlines = [RetiradaCestaBasicaInline]

    def contagem_retiradas(self, obj):
        return obj.contagem_retiradas()
    contagem_retiradas.short_description = 'Número de Retiradas'

admin.site.register(Beneficiario, BeneficiarioAdmin)
