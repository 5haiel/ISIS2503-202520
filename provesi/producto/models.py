from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.IntegerField(null=True, blank=True, default=None)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
