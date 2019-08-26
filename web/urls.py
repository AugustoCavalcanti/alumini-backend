from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import *

router = routers.DefaultRouter()
router.register(r'turmas', TurmaViewSet, basename='turmas')
router.register(r'formandos', FormandoViewSet, basename='formandos')
router.register(r'habilidades', HabilidadeViewSet, basename='habilidades')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('pesquisa/', PesquisaView.as_view(), name='pesquisa'),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]
