from django.contrib import admin

# Register your models here.
from .models import Beneficiario
from django.utils.translation import gettext_lazy as _

admin.site.site_header = _("Nome da Sua Igreja - Admin")
admin.site.site_title = _("Nome da Sua Igreja")
admin.site.index_title = _("Bem-vindo ao Painel de Administração da Sua Igreja")

@admin.register(Beneficiario)
class BeneficiarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf','endereco', 'qtd_membros_familia', 'data_cadastro', 'data_nascimento')
    search_fields = ('nome',)
    list_filter = ('data_cadastro', 'qtd_membros_familia')