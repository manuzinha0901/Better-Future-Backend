from django.shortcuts import render
from rest_framework import viewsets
from cursos.models import Cursos
from cursos.serializers import CursosSerializers

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializers


# Create your views here.
