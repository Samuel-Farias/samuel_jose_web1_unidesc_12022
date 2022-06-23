from django.db import models

# Create your models here.
class locacao(models.Model):

	dataDesocupacao = models.DateField(max_length=100)
	periodo = models.DateField(max_length=100)

def __str__(self):
	return self.dataDesocupacao