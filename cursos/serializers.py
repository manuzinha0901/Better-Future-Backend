from rest_framework import serializers
from cursos.models import Cursos


class CursosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = ['id','nome_curso','tipo_curso','carga_horaria','vagas_disponiveis','quantidades_turmas', 'horarios','professor','conteudo_curso']