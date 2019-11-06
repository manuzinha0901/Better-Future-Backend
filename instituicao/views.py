from django.shortcuts import render
from rest_framework import viewsets
from instituicao.models import Instituicao
from instituicao.serializers import InstituicaoSerializers

class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializers