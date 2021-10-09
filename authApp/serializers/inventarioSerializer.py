from rest_framework import serializers
from authApp.models.inventario import Inventario


class InventarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inventario
        fields = '__all__'
    def create(self, validated_data):

        return Inventario.objects.create(**validated_data)

    def to_representation(self, obj):
        inventario = Inventario.objects.get(id=obj.id)
        return {
            'id': inventario.id,
            'nombre': inventario.nombre,
            'tipo': inventario.tipo,
            'existencia': inventario.existencia,
            'lastChangeDate': inventario.lastChangeDate,
            'isActive': inventario.isActive,
            
        }
    def update(self,instance,validated_data):
        
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.tipo = validated_data.get('tipo',instance.tipo)
        instance.existencia = validated_data.get('existencia',instance.existencia)
        instance.isActive = validated_data.get('isActive',instance.isActive)
        
        instance.save()
        return instance