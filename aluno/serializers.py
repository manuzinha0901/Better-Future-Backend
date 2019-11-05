from rest_framework import serializers
from aluno.models import Aluno


class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','sobrenome','data', 'endereco', 'complemento','celular', 'email','senha',
        'confirmar_senha']