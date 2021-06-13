from rest_framework import serializers

from .models import Avaliacao, Departamento, Disciplina, Professor


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = (
            "id",
            "name",
            "get_absolute_url",
        )


class DepartamentoSerializer(serializers.ModelSerializer):
    disciplinas = DisciplinaSerializer(many=True)

    class Meta:
        model = Departamento
        fields = (
            "id",
            "name",
            "disciplinas",
            "get_absolute_url",
        )


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = (
            "id",
            "name",
            "email",
            "get_absolute_url",
        )


class AvaliacaoSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer()
    disciplina = DisciplinaSerializer()

    class Meta:
        model = Avaliacao
        fields = (
            "id",
            "semestre",
            "disciplina",
            "professor",
            "nota",
        )
