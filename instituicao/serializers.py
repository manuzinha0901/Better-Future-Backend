from rest_framework import serializers
from instituicao.models import Instituicao


class InstituicaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = ['id','nome','responsavel','endereco', 'cep', 'numero', 'email','senha',]