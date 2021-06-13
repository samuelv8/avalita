from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Avaliacao, Departamento, Disciplina, Professor
from .serializers import AvaliacaoSerializer, DepartamentoSerializer, DisciplinaSerializer, MediaSerializer


class LatestDisciplinasList(APIView):
    def get(self, request, format=None):
        disciplinas = Disciplina.objects.all()[0:4]
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data)


class AllDepartamentos(APIView):
    def get(self, request, format=None):
        departamentos = Departamento.objects.all().order_by('slug')
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)


class AllAvaliacoes(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class BestMedias(APIView):
    def get(self, request, format=None):
        avaliacoes = Avaliacao.objects.all()
        notas = dict()
        for avaliacao in avaliacoes:
            key = (avaliacao.disciplina, avaliacao.professor)
            nota = avaliacao.nota
            notas.setdefault(key, []).append(nota)
        medias = list(
            {
                'disciplina': k[0],
                'professor': k[1],
                'nota': round(sum(v)/len(v), 2),
                'count': len(v),
            } for (k, v) in notas.items())
        medias.sort(key=lambda x: x['nota'], reverse=True)
        serializer = MediaSerializer(medias, many=True)
        return Response(serializer.data)


class DepartamentoDetail(APIView):
    def get_object(self, departamento_slug):
        try:
            return Departamento.objects.get(slug=departamento_slug)
        except Departamento.DoesNotExist:
            raise Http404

    def get(self, request, departamento_slug, format=None):
        departamento = self.get_object(departamento_slug)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)
