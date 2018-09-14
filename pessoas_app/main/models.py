from django.db import models

# Create your models here.
class Pessoa(models.Model):
  nome = models.TextField()
  cpf = models.IntegerField()