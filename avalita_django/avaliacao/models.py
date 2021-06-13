from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=80)
    slug = models.SlugField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return f'/dpto/{self.slug}/'
