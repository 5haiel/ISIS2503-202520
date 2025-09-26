from django import forms
from .models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = [
            'producto',
            'bodega',
            'ubicacion',
            'stock',
        ]

        labels = {
            'product' : 'Pariable',
            'bodega' : 'Bodega',
            'ubicacion' : 'Ubicacion',
            'stock' : 'Stock',
        }