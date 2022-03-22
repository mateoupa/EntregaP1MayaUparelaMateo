from django.db import models

# Create your models here.


class auditor(models.Model):
    nombre = models.CharField(max_length=20)
    cargo = models.CharField(max_length=20)
    email = models.EmailField()
    
class registro_producto(models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()
    cantidad =models.IntegerField()
    
    def __str__(self):
        return f'Has encontrado el siguiente producto --> {self.nombre} <-- con precio {self.precio} y cantidad existente {self.cantidad}'
    
    
class almacen(models.Model):
    nombre = models.CharField(max_length=20)
    turno = models.IntegerField()
    