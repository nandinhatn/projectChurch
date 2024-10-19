from django.db import models

# Create your models here.
# retiradas_cestas_basicas/models.py

from django.db import models
from cestas_basicas.models import CadastroCestaBasica
from beneficiarios.models import Beneficiario  # Supondo que esse modelo exista

class RetiradaCestaBasica(models.Model):
    id_retira = models.AutoField(primary_key=True)
    data_retira = models.DateField(auto_now_add=True)
    id_beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Retirada {self.id_retira} - Beneficiário {self.id_beneficiario}'
