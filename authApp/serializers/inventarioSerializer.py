from rest_framework import serializers
from authApp.models.inventario import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventario
        fields = ['id', 'nombre', 'tipo','existencia','lastChangeDate','isActive']