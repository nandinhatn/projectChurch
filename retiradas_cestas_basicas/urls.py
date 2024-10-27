# retiradas_cestas_basicas/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RetiradaCestaBasicaViewSet

router = DefaultRouter()
router.register(r'retiradas', RetiradaCestaBasicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
