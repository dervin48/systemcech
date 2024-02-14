from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
