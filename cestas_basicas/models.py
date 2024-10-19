from django.db import models

# Create your models here.

# Register your models here.

class CadastroCestaBasica(models.Model):
    cesta_qtd = models.IntegerField()


    def __str__(self):
        return f"Cesta Básica :{self.cesta_qtd}"
