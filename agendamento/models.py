from django.db import models

# Create your models here.
class agendamento(models.Model):
    dia = models.DateField(max_length=100)
    hora = models.DateField(max_length=100)
    local = models.CharField(max_length=100)
    
def incluir_Agendamento(): void
def consultar_Agendamento(): Double
def alterar_Agendamento(): void
def remover_Agendamento(): void
def __str__(self):
	return self.dia

    