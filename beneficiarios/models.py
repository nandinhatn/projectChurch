from django.db import models

# Create your models here.
class Beneficiario(models.Model):
    cpf = models.CharField(max_length=14, unique=True)  # O CPF tem 11 dígitos, mas aqui consideramos o formato com pontuação
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    qtd_membros_familia = models.IntegerField()
    data_cadastro = models.DateField(auto_now_add=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome