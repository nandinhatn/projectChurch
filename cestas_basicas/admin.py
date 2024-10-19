from django.contrib import admin
from django.contrib import messages
from .models import CadastroCestaBasica
from .forms import CadastroCestaBasicaForm

@admin.register(CadastroCestaBasica)
class CadastroCestaBasicaAdmin(admin.ModelAdmin):
    form = CadastroCestaBasicaForm
    list_display = ('id', 'cesta_qtd')
    
    # Impede a edição direta da quantidade de cestas no admin
    def get_readonly_fields(self, request, obj=None):
        return ['cesta_qtd']

    # Impede a criação de novas instâncias
    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        # Lógica para adicionar ou remover cestas
        adicionar_cesta = form.cleaned_data.get('adicionar_cesta', 0)
        remover_cesta = form.cleaned_data.get('remover_cesta', 0)

        if adicionar_cesta:
            obj.cesta_qtd += adicionar_cesta  # Adiciona a quantidade especificada
            messages.success(request, f'Adicionou {adicionar_cesta} cestas para {obj.id}.')

        if remover_cesta:
            if obj.cesta_qtd >= remover_cesta:
                obj.cesta_qtd -= remover_cesta  # Remove a quantidade especificada
                messages.success(request, f'Removeu {remover_cesta} cestas de {obj.id}.')
            else:
                messages.warning(request, f'Não é possível remover {remover_cesta} cestas de {obj.id}, pois a quantidade atual é {obj.cesta_qtd}.')

        # Salva as alterações
        obj.save()

    # Remover a opção de deletar no admin
    def has_delete_permission(self, request, obj=None):
        return False
