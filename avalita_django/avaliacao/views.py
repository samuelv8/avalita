from avalita_django.avaliacao.serializers import DisciplinaSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Disciplina


class LatestDisciplinasList(APIView):
    def get(self, request, format=None):
        disciplinas = Disciplina.objects.all()[0:4]
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)
