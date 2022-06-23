from tokenize import Double
from django.db import models

# Create your models here.
class funcionario(models.Model):
    
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=100)
    sexo = models.CharField(max_length=100)
    carteira = models.CharField(max_length=100)
    salario = models.IntegerField(max_length=100)
    pis = models.CharField(max_length=100)
def consultar_Imoveis(): Double

def __str__(self):
	return self.cpf