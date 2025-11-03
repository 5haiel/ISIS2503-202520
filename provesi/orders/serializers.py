from rest_framework import serializers
from .models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source="producto.nombre", read_only=True)
    usuario_id = serializers.IntegerField(source="usuario.id_usuario", read_only=False)

    class Meta:
        model = Orders
        fields = ['id', 'usuario_id', 'producto', 'producto_nombre', 'cantidad', 'ubicacion']
