from django.shortcuts import render
from .models import Filme

# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def vizualizar(request):
    filme = Filme.objects.all()
    return render(request, "vizualizar.html", {"filme": filme})
