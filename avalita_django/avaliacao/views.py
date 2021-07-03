from django.db.models import query
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Avaliacao, Departamento, Disciplina, Professor
from .serializers import AvaliacaoSerializer, DepartamentoSerializer, DisciplinaSerializer, MediaSerializer, \
    ProfessorSerializer


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
                'nota': round(sum(v) / len(v), 2),
                'count': len(v),
            } for (k, v) in notas.items())
        medias.sort(key=lambda x: x['nota'], reverse=True)
        serializer = MediaSerializer(medias, many=True)
        return Response(serializer.data)


class BestMediasDepartamento(APIView):
    def get(self, request, departamento_slug, disciplina_slug, format=None):
        avaliacoes = Avaliacao.objects \
            .filter(disciplina__departamento__slug=departamento_slug) \
            .filter(disciplina__slug=disciplina_slug)
        notas = dict()
        for avaliacao in avaliacoes:
            key = (avaliacao.disciplina, avaliacao.professor)
            nota = avaliacao.nota
            notas.setdefault(key, []).append(nota)
        medias = list(
            {
                'disciplina': k[0],
                'professor': k[1],
                'nota': round(sum(v) / len(v), 2),
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


class DisciplinaDetail(APIView):
    def get_object(self, departamento_slug, disciplina_slug):
        try:
            return Disciplina.objects.filter(departamento__slug=departamento_slug).get(slug=disciplina_slug)
        except Disciplina.DoesNotExist:
            raise Http404

    def get(self, request, departamento_slug, disciplina_slug, format=None):
        disciplina = self.get_object(departamento_slug, disciplina_slug)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)


class ProfessoresDisciplina(APIView):
    def get_object(self, departamento_slug, disciplina_slug):
        try:
            return Disciplina.objects.filter(departamento__slug=departamento_slug).get(slug=disciplina_slug)
        except Disciplina.DoesNotExist:
            raise Http404

    def get(self, request, departamento_slug, disciplina_slug, format=None):
        disciplina = self.get_object(departamento_slug, disciplina_slug)
        professores = set(
            map(lambda a: a.professor, disciplina.avaliacoes.all()))
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data)


class MyAvaliacoes(APIView):
    def get(self, request, format=None):
        my_avals = Avaliacao.objects.filter(user=request.user)
        serializer = AvaliacaoSerializer(my_avals, many=True)
        return Response(serializer.data)


class SubmitAvaliacao(APIView):
    def post(self, request):
        user = request.user
        disciplina = request.data.get("disciplina")
        professor = request.data.get("professor")
        nota = request.data.get("nota")

        disciplina = get_object_or_404(Disciplina, slug__iexact=disciplina)
        professor = get_object_or_404(Professor, name__iexact=professor)

        avaliacao = Avaliacao(user=user, disciplina=disciplina, professor=professor, nota=nota)
        if not Avaliacao.objects.filter(user=user, disciplina=disciplina, professor=professor):
            avaliacao.save()
            return Response({"success": True})

        return Response(status=status.HTTP_403_FORBIDDEN)


class DeleteAvaliacao(APIView):
    def delete(self, request):
        id = request.data.get("id")
        aval_to_delete = Avaliacao.objects.get(id=id)
        aval_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    