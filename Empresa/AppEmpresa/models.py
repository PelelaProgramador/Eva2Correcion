from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=50)
    litro = models.CharField(max_length=50)
    tamanio = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=50)
    tipoagua = models.CharField(max_length=50)