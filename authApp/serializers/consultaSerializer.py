from rest_framework import serializers
from authApp.models.consulta import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

        def create(self, validated_data):
        
            return Consulta.objects.create(**validated_data)

        def to_representation(self, obj):
            consulta = Consulta.objects.get(id=obj.id)
            return {
                'id': consulta.id,
                'idUsu': consulta.idUsu,
                'idInv': consulta.idInv,
                'registro': consulta.registro,
            }