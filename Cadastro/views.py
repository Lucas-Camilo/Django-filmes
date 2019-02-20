from django.shortcuts import render, HttpResponse
from .models import Filme
# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def visualizar(request):
    filme = Filme()
    return render(request, "vizualizar.html")
