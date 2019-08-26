from .models import *
from rest_framework import serializers


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = '__all__'


class FormandoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formando
        fields = '__all__'

    habilidades = HabilidadeSerializer(many=True, read_only=True)

