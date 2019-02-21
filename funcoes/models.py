from django.db import models

# Create your models here.
class Filme(models.Model):
    Nome = models.CharField(max_length=30)
    Descricao = models.TextField()
    Url = models.TextField()
