from django.db import models
from producto.models import Producto

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="orders")
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        nombre = getattr(self.producto, "nombre", str(self.producto))
        return f"{nombre} x {self.cantidad} @ {self.ubicacion}"