from django.db import models

# Create your models here.

class pessoa(models.Model):

	matricula = models.IntegerField(max_length=100)
	tel = models.CharField(max_length=100)
	cep = models.CharField(max_length=100)

def __str__(self):
	return self.matricula
