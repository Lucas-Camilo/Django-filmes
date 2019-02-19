from django.shortcuts import render, HttpResponse
from random import randint
import os
# Create your views here.
def home(request):
    """
    pasta_fundo = "../static/img/fundo/"
    fundos = []
    for file in os.listdir(pasta_fundo):
        fundos.append(file)
    fundos = fundos[randint(0, 1)]
    """
    return render(request, "funcionalidades.html")
def visualizar(request):
    return render(request, "vizualizar.html")
