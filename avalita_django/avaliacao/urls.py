from django.urls import path

from avaliacao import views


urlpatterns = [
    path('latest-disciplinas/', views.LatestDisciplinasList.as_view()),
    path('best-medias/', views.BestMedias.as_view()),
    path('all-avaliacoes/', views.AllAvaliacoes.as_view()),
    path('all-departamentos/', views.AllDepartamentos.as_view()),
]
