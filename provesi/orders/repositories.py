from .models import Orders
from producto.models import Producto

def get_order_with_product_and_location(order_id: int) -> dict:
    # Traer campos del pedido
    order_qs = Orders.objects.filter(pk=order_id).select_related("producto").values(
        "id", "cantidad", "ubicacion",
        "producto__id", "producto__nombre", "producto__sku"
    ).first()
    if not order_qs:
        return None

    # Normalizar a estructura deseada
    result = {
        "id": order_qs["id"],
        "cantidad": order_qs["cantidad"],
        "ubicacion": order_qs["ubicacion"],
        "producto": {
            "id": order_qs["producto__id"],
            "nombre": order_qs.get("producto__nombre"),
            "sku": order_qs.get("producto__sku"),
        }
    }
    return result
