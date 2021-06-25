from rest_framework import serializers

from .models import Avaliacao, Departamento, Disciplina, Professor


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "slug",
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
            "disciplina",
            "professor",
            "nota",
        )


class MediaSerializer(serializers.Serializer):
    nota = serializers.DecimalField(max_digits=3, decimal_places=2)
    count = serializers.IntegerField()
    disciplina = DisciplinaSerializer()
    professor = ProfessorSerializer()

    class Meta:
        fields = (
            "nota",
            "count",
            "disciplina",
            "professor",
        )
