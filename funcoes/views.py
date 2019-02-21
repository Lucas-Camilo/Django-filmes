from django.shortcuts import render
from .models import Filme
from .forms import Cadastro

# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def vizualizar(request):
    filme = Filme.objects.all()
    return render(request, "vizualizar.html", {"filme": filme})
def cadastro(request):
    form = Cadastro(request.Get)
    nome = request.get("fname")
    descrica = request.get("desc")
    url = request.get("url")
    return render(request, "home.html",
                  {"form": form, "nome": nome, "url": url, "desc": descrica})
