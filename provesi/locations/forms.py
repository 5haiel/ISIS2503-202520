from django import forms
from .models import Location

class LocationForms(forms.ModelForm):
    class Meta:
        model = Location
        fields = [
            'producto',
            'bodega',
            'estante',
        ]

        labels = {
            'producto' : 'Producto',
            'bodega' : 'Bodega',
            'estante' : 'Estante',
    
        }