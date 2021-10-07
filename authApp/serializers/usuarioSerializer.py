from rest_framework import serializers
from authApp.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):

        return Usuario.objects.create(**validated_data)

    def to_representation(self, obj):
        user = Usuario.objects.get(id=obj.id)
        
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'apellido': user.apellido,
            'fechaNacimiento': user.fechaNacimiento,
            'celular': user.celular,
            'email': user.email,
            'rol': user.rol,
            'estado': user.estado,
            'fechaRegistro': user.fechaRegistro,
            
        }