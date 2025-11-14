from django.db import models

class Usuario(models.Model):
    # Identificación básica
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion_entrega = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10, blank=True, null=True)
    pais = models.CharField(max_length=100, default='Colombia')

    def __str__(self):
        return f"{self.nombre} ({self.correo})"
