from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    return render(request, "funcionalidades.html")
def visualizar(request):
    return render(request, "vizualizar.html")
