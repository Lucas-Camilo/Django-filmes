from django.db import models

# Create your models here.
class Filme(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
