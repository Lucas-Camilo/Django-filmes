from django.shortcuts import render
from .models import Filme

# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def vizualizar(request):
    filme = Filme.objects.all()
    return render(request, "vizualizar.html", {"filme": filme})
def cadastro(request):
    nome = request.get("fname")
    descrica = request.get("desc")
    url = request.get("url")
    """if request.method == 'Post':
            Filme.objects.create(Nome="", Descricao="", Url="")"""
    return render(request, "home.html", {"nome": nome, "url": url, "desc": descrica})
