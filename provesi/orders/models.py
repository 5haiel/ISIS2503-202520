from django.db import models
from producto.models import Producto
from users.models import Usuario;

# Create your models here.
class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.PositiveIntegerField()
    ubicacion = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="orders")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="orders")

class Meta:
        db_table = 'ordenes'
        managed  = False   