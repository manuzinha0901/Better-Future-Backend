from rest_framework import serializers
from cursos.models import Cursos


class CursosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['id','nome_curso','carga_horaria','vagas_disponiveis', 'horarios',]