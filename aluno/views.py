from django.shortcuts import render
from rest_framework import viewsets
from aluno.models import Aluno
from aluno.serializers import AlunoSerializers

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializers












# Create your views here.
