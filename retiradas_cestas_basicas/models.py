from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from beneficiarios.models import Beneficiario

class RetiradaCestaBasica(models.Model):
    id_retira = models.AutoField(primary_key=True)
    beneficiario = models.ForeignKey(
        Beneficiario, 
        on_delete=models.CASCADE, 
        related_name='retiradas'
    )
    data_retira = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Retirada de Cesta Básica'
        verbose_name_plural = 'Retiradas de Cestas Básicas'
    
    def clean(self):
        um_mes_atras = timezone.now() - timezone.timedelta(days=30)
        if self.beneficiario.retiradas.filter(data_retira__gte=um_mes_atras).exists():
            # Levanta um ValidationError se já houver uma retirada no último mês
            raise ValidationError(f'O beneficiário {self.beneficiario.nome} já retirou uma cesta no último mês.')

    def save(self, *args, **kwargs):
        # Chama o método clean antes de salvar
        self.clean()  # Isso irá levantar um erro se não for válido
        super().save(*args, **kwargs)

    def __str__(self):
        result = f'Retirada {self.id_retira} - {self.beneficiario.nome} em {self.data_retira}'
        print("dentro do str")  # Adicione esta linha para depuração
        print(result)  # Adicione esta linha para depuração
        return result