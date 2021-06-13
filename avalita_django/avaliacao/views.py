
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Avaliacao, Disciplina
from .serializers import AvaliacaoSerializer, DisciplinaSerializer


class LatestDisciplinasList(APIView):
    def get(self, request, format=None):
        disciplinas = Disciplina.objects.all()[0:4]
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)


class AllAvaliacoes(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)
