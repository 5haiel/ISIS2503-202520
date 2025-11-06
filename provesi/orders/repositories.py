from .models import Orders
from producto.models import Producto

def get_order_with_product_and_location(order_id: int) -> dict | None:
    row = (
        Orders.objects
        .filter(pk=order_id)
        .values(
            "id", "cantidad", "ubicacion",
            "producto_id", "producto__nombre", "producto__sku",
            "usuario_id", "usuario__nombre", "usuario__correo", "usuario__direccion_entrega",
        )
        .first()
    )
    if not row:
        return None

    return {
        "id": row["id"],
        "cantidad": row.get("cantidad"),
        "ubicacion": row.get("ubicacion"),
        "producto": None if row.get("producto_id") is None else {
            "id": row.get("producto_id"),
            "nombre": row.get("producto__nombre"),
            "sku": row.get("producto__sku"),
        },
        "usuario": None if row.get("usuario_id") is None else {
            "id": row.get("usuario_id"),
            "nombre": row.get("usuario__nombre"),
            "correo": row.get("usuario__correo"),
            "direccion_entrega": row.get("usuario__direccion_entrega"),
        },
    }
