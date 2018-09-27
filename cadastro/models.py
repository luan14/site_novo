from django.db import models
from django.utils import timezone
class Jogos (models.Model):
    nome_jogo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    produtora = models.ForeignKey('Produtora', on_delete=models.CASCADE)
    desenvolvedora = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome_jogo

class Produtora(models.Model):
    nomeProdutora = models.CharField(max_length=25)

    def __str__(self):
        return self.nomeProdutora


