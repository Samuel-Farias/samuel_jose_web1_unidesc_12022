from django.db import models

# Create your models here.
class aviso(models.Model):
    matricula_avi = models.IntegerField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.CharField(max_length=100)
    
def incluir_Aviso(): void
def consultar_Aviso(): Double
def remover_Aviso(): void
def __str__(self):
	return self.matricula_avi