from django.db import models


class Cursos(models.Model):
    nome_curso = models.CharField(max_length=255)
    carga_horaria = models.CharField(max_length=255)
    vagas_disponiveis= models.CharField(max_length=255)
    horarios = models.CharField(max_length=255)


# Create your models here.
