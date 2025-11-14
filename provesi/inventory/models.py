from django.db import models
from producto.models import Producto

class Inventory(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    bodega = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '%s %s' % (self.producto, self.stock)
    
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)