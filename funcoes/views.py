from django.shortcuts import render
from .models import Filme
from .forms import Cadastro

# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def visualizar(request):
    filme = Filme.objects.all()
    return render(request, "vizualizar.html", {"filme": filme})
def cadastro(request):
    nome = request.GET.get("fname")
    desc = request.GET.get("desc")
    url = request.GET.get("url")
    Filme.objects.create(Nome=nome, Descricao=desc, Url=url)
    return render(request, "home.html", {"status": "Adcionado com sucesso"})
def excluir(request):
    nome = request.GET.get("fname")
    Filme.objects.filter(Nome=nome).delete()
    return render(request, "home.html", {"status": "Excluido"})
def atualizar(request):
    nome = request.GET.get("fname")
    desc = request.GET.get("desc")
    Filme.objects.filter(Nome=nome).update(Descricao=desc)
    return render(request, "home.html", {"status": "Atualizado com sucesso"})
