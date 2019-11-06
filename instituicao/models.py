from django.db import models


class Instituicao(models.Model):
    nome = models.CharField(max_length=255)
    responsavel = models.CharField(max_length=255)
    endereco= models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

# Create your models here.
