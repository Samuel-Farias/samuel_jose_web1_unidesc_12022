from wsgiref.validate import validator
from django.db import models

# Create your models here.
class imovel(models.Model):

	mareicula_Imo = models.IntegerField(max_length=100)
	vaor = models.IntegerField(max_length=100)
	
def incluir_Anuncio(): void
def __str__(self):
	return self.nome