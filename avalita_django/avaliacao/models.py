from django.db import models


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
        return self.name

    def get_absolute_url(self):
        return f'/dpto/{self.departamento.slug}/{self.slug}'
