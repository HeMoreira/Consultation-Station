from django.urls import path
from . import views

urlpatterns = [
    path('novaconsulta/', views.nova_consulta, name='nova_consulta'),
    path('cronogramadeconsultas/', views.cronograma_consultas, name='cronograma_consultas'),
    path('view/<int:pk>/', views.detalhes_consulta, name='detalhes_consulta'),
    path('edit/<int:pk>/', views.editar_consulta, name='editar_consulta'),
    path('delete/<int:pk>/', views.deletar_consulta, name='deletar_consulta'),
    path('failure/', views.failure, name='failure'),
]