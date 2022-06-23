from django.db import models

# Create your models here.
class pagamento(models.Model):

	valor_pg = models.IntegerField(max_length=100)
	forma_pg = models.CharField(max_length=100)
	parcelas_pg = models.IntegerField(max_length=100)
    

def __str__(self):
	return self.valo_pg