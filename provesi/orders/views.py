# orders/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Orders
# from .models import Orders  # ajusta el import a tu modelo real

def order_detail_view(request, id: int):
    o = get_object_or_404(
        Orders.objects.select_related('producto', 'usuario'),
        pk=id
    )

    # Si quieres devolver JSON simple:
    payload = {
        "id": o.pk,
        "cantidad": getattr(o, "cantidad", None),
        "ubicacion": getattr(o, "ubicacion", None),
        "producto": None if o.producto is None else {
            "id": getattr(o.producto, "pk", None),
            "nombre": getattr(o.producto, "nombre", None),
            "sku": getattr(o.producto, "sku", None),
        },
        "usuario": None if o.usuario is None else {
            "id": getattr(o.usuario, "pk", None),
            "nombre": getattr(o.usuario, "nombre", None),
            "correo": getattr(o.usuario, "correo", None),
            "direccion_entrega": getattr(o.usuario, "direccion_entrega", None),
        },
    }
    return JsonResponse(payload, status=200)
