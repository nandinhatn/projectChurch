from django.shortcuts import render

# Create your views here.
# retiradas_cestas_basicas/views.py

from rest_framework import viewsets
from .models import RetiradaCestaBasica
from .serializers import RetiradaCestaBasicaSerializer
from rest_framework.response import Response
from rest_framework import status
from cestas_basicas.models import CadastroCestaBasica

class RetiradaCestaBasicaViewSet(viewsets.ModelViewSet):
    queryset = RetiradaCestaBasica.objects.all()
    serializer_class = RetiradaCestaBasicaSerializer

    def create(self, request, *args, **kwargs):
        # Verifica se há cestas disponíveis
        cestas_disponiveis = CadastroCestaBasica.objects.first()  # Ajuste conforme necessário para pegar a cesta certa

        if cestas_disponiveis and cestas_disponiveis.cesta_qtd > 0:
            # Cria a retirada
            return super().create(request, *args, **kwargs)
        else:
            return Response({'error': 'Não há cestas disponíveis para retirada.'}, status=status.HTTP_400_BAD_REQUEST)
