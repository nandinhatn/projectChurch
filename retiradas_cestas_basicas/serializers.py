# retiradas_cestas_basicas/serializers.py

from rest_framework import serializers
from .models import RetiradaCestaBasica

class RetiradaCestaBasicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetiradaCestaBasica
        fields = '__all__'
