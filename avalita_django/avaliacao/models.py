from django.contrib.auth.models import User
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator


class Departamento(models.Model):
    name = models.CharField(max_length=80)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/dpto/{self.slug}/'


class Disciplina(models.Model):
    departamento = models.ForeignKey(
        Departamento, related_name='disciplinas', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return f'/dpto/{self.departamento.slug}/{self.slug}'


class Professor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/professor/{self.pk}/'


class Avaliacao(models.Model):
    user = models.ForeignKey(
        User, related_name='avaliacoes', on_delete=models.CASCADE)
    semestre = models.CharField(max_length=6)
    disciplina = models.ForeignKey(
        Disciplina, related_name='avaliacoes', on_delete=models.CASCADE)
    professor = models.ForeignKey(
        Professor, related_name='avaliacoes', on_delete=models.CASCADE)
    nota = models.DecimalField(
        max_digits=2, decimal_places=1,
        default=1.0,
        validators=[
            MaxValueValidator(5.0),
            MinValueValidator(1.0)
        ])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return str(self.pk) + ' ' + str(self.disciplina)

    def get_absolute_url(self):
        return f'/dpto/{self.departamento.slug}/{self.slug}'
