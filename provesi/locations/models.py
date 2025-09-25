from django.db import models


class Location (models.Model):
    producto = models.FloatField(null=True, blank=True, default=None)
    bodega = models.IntegerField(null=True, blank=True, default=None)
    estante = models.IntegerField(null=True, blank=True, default=None)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)
