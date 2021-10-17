from rest_framework import serializers
from authApp.models.consulta import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'idUsu', 'idInv','registro']