from django.urls import path
from . import views

urlpatterns = [
    path('novaconsulta/', views.nova_consulta, name='nova_consulta'),
    path('cronogramadeconsultas/', views.cronograma_consultas, name='cronograma_consultas'),
    path('failure/', views.failure, name='failure'),
]