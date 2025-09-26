from django.db import models
from .models import Inventory

def total_disponible(producto_id, bodega: str):
    qs = Inventory.objects.filter(bodega=bodega)
    if producto_id is not None:
        qs = qs.filter(producto_id=producto_id)
    return qs.aggregate(total=models.Sum("stock"))["total"] or 0

def primera_ubicacion_con_stock(producto_id, bodega: str, cantidad: int):
    qs = Inventory.objects.filter(bodega=bodega)
    if producto_id is not None:
        qs = qs.filter(producto_id=producto_id)
    return qs.filter(stock__gte=cantidad).order_by("-stock").first()
