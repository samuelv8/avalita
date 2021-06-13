from django.db import models
from rest_framework import serializers

from .models import Departamento, Disciplina


class DisciplinaSerializer:
    class Meta:
        model = Disciplina
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "get_image",
            "thumbnail",
        )
