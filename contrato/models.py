from django.db import models

# Create your models here.
class contrato(models.Model):
    dadosCliente = models.CharField(max_length=100)
    dadosCorretor = models.CharField(max_length=100)
    descricaoImovel = models.CharField(max_length=100)
    documentacao = models.CharField(max_length=100)
    
def __str__(self):
	return self.dia
