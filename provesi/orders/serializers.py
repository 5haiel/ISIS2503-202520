from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)

    class Meta:
        model = Orders
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'ubicacion']
