from rest_framework import serializers
from .models import Curso, Avalicacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        #O campo email sera utilizando somente para escrita, assim o email não fica exposto na API
        extra_kwargs = {
            'email':{'write_only':True}
        }
        model = Avalicacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'ativo'
        )
        
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'ativo'
        )