from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    search_fields = ['nome']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = ['nome']


class FormandoViewSet(viewsets.ModelViewSet):
    queryset = Formando.objects.all()
    serializer_class = FormandoSerializer
    search_fields = ['nome']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = ['nome']


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer
    search_fields = ['nome']
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = '__all__'
    ordering_fields = ['nome']


class PesquisaView(APIView):
    def get(self, request):
        search = self.request.query_params.get('search', None)
        if search is not None:
            turmas = Turma.objects.filter(Q(nome_icontains=search) | Q(ano_icontains=search))
            formandos = Formando.objects.filter(Q(nome_icontains=search) | Q(destaque_icontains=search) | Q(ocupacao_icontains=search) | Q(formacao_icontains=search) | Q(local_icontains=search) | Q(habilidades_icontains=search))
            habilidades = Habilidade.objects.filter(Q(nome_icontains=search))

            turmas_data = TurmaSerializer(turmas, many=True).data
            formandos_data = FormandoSerializer(formandos, many=True).data
            habilidades_data = HabilidadeSerializer(habilidades, many=True).data

            return Response({'results': {
                'turmas': turmas_data,
                'formandos': formandos_data,
                'habilidades': habilidades_data
            }}, 200)
        else:
            return Response({'results': {'turmas': None,
                                         'formandos': None,
                                         'habilidades': None}}, 200)

