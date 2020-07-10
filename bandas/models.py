from django.db import models


class Banda(models.Model):
    nome = models.CharField(max_length=50)
    integrantes = models.IntegerField()
    ano_fundacao = models.IntegerField()

    def __str__(self):
        return f"Nome: {self.nome} / Integrantes: {self.integrantes} / Ano fundação: {self.ano_fundacao}"


class Album(models.Model):
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    nome = models.CharField(max_length=60)
    ano_lancamento = models.IntegerField()

    def __str__(self):
        return self.nome
