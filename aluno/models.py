from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    data = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    celular = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    confirmar_senha = models.CharField(max_length=255)

# Create your models here.
