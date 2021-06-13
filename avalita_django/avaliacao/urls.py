from django.urls import path

from avaliacao import views


urlpatterns = [
    path('latest-disciplinas/', views.LatestDisciplinasList.as_view())
]
