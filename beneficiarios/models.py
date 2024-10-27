from django.db import models

class Beneficiario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    endereco = models.CharField(max_length=255)
    qtd_membros_familia = models.IntegerField()
    data_cadastro = models.DateField(auto_now_add=True)
    data_nascimento = models.DateField(null=True, blank=True)  # Novo campo opcional

    def contagem_retiradas(self):
        return self.retiradas.count()

    def __str__(self):
        return self.nome
