from django.urls import path

from . import views

urlpatterns = [
    path('latest-disciplinas/', views.LatestDisciplinasList.as_view()),
    path('best-medias/', views.BestMedias.as_view()),
    path('all-avaliacoes/', views.AllAvaliacoes.as_view()),
    path('all-departamentos/', views.AllDepartamentos.as_view()),
    path('best-medias/<slug:departamento_slug>/<slug:disciplina_slug>/', views.BestMediasDepartamento.as_view()),
    path('dpto/<slug:departamento_slug>/', views.DepartamentoDetail.as_view()),
    path('dpto/<slug:departamento_slug>/<slug:disciplina_slug>/',
         views.DisciplinaDetail.as_view()),
    path('dpto/<slug:departamento_slug>/<slug:disciplina_slug>/p/',
         views.ProfessoresDisciplina.as_view()),
    path('my-avals/', views.MyAvaliacoes.as_view()),
    path('submit-avaliacao/', views.SubmitAvaliacao.as_view()),
    path('delete-avaliacao/', views.DeleteAvaliacao.as_view()),
]
