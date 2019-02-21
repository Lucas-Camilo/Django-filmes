from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('visualizar/', views.visualizar),
    path('cadastro/', views.cadastro),
    path('excluir', views.excluir),
    path('atualizar', views.atualizar)
]
