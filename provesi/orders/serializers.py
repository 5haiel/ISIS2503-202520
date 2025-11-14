from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    # Extras de solo lectura
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)
    usuario_id = serializers.IntegerField(source="usuario.pk", read_only=True)

    class Meta:
        model = Orders
        fields = [
            'id',
            'usuario',         
            'usuario_id',    
            'producto', 
            'producto_nombre',
            'cantidad',
            'ubicacion',
        ]
