from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('vizualizar/', views.vizualizar),
    path('cadastro/', views.cadastro),
    path('excluir', views.excluir),
]
