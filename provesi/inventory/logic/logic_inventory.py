
from ..models import Inventory
def get_inventory():
    queryset = Inventory.objects.all().order_by('-id')[:10]

def create_inventory(form):
    inventory = form.save()
    return inventory

def create_inventory_object(bodega, ubicacion, stock, producto_id=None):
    inventory = Inventory(
        producto_id=producto_id,  
        bodega=bodega,
        ubicacion=ubicacion,
        stock=int(stock)
    )
    inventory.save()
    return inventory