from django.shortcuts import render
from .models import Filme

# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def vizualizar(request):
    filme = Filme.objects.all()
    return render(request, "vizualizar.html", {"filme": filme})
def cadastro(request):
    nome = request.Post.get("fname")
    descrica = request.Post.get("desc")
    url = request.Post.get("url")
    """if request.method == 'Post':
            Filme.objects.create(Nome="", Descricao="", Url="")"""
    return render(request, "home.html", {"nome": nome, "url": url, "desc": descrica})
