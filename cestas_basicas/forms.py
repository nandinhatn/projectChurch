# forms.py
from django import forms
from .models import CadastroCestaBasica

class CadastroCestaBasicaForm(forms.ModelForm):
    adicionar_cesta = forms.IntegerField(required=False, min_value=0, label="Adicionar Cesta Básica")
    remover_cesta = forms.IntegerField(required=False, min_value=0, label="Remover Cesta Básica")

    class Meta:
        model = CadastroCestaBasica
        fields = ['cesta_qtd', 'adicionar_cesta', 'remover_cesta']

    def clean(self):
        cleaned_data = super().clean()
        adicionar_cesta = cleaned_data.get("adicionar_cesta")
        remover_cesta = cleaned_data.get("remover_cesta")

        # Permitir que apenas um dos campos seja preenchido
        if not adicionar_cesta and not remover_cesta:
            raise forms.ValidationError("Você deve adicionar ou remover cestas básicas.")

        return cleaned_data
