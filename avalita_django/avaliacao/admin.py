from django.contrib import admin

from .models import Avaliacao, Departamento, Disciplina, Professor

admin.site.register(Departamento)
admin.site.register(Disciplina)
admin.site.register(Avaliacao)
admin.site.register(Professor)
