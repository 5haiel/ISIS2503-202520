
from .selectors import total_disponible, primera_ubicacion_con_stock

def sugerir_ubicacion(producto_id, bodega: str, cantidad: int):
    disponible = total_disponible(producto_id, bodega)
    ubi = None
    if disponible >= cantidad:
        fila = primera_ubicacion_con_stock(producto_id, bodega, cantidad)
        if fila:
            ubi = fila.ubicacion
    return {"disponible": disponible, "ubicacion_sugerida": ubi}
