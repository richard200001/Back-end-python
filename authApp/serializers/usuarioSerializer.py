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
            'nombre': user.nombre,
            'apellido': user.apellido,
            'fechaNacimiento': user.fechaNacimiento,
            'celular': user.celular,
            'email': user.email,
            'rol': user.rol,
            'estado': user.estado,
            'fechaRegistro': user.fechaRegistro,
            
        }
    def update(self,instance,validated_data):
        
        instance.nombre = validated_data.get('nombre',instance.nombre)
        instance.apellido = validated_data.get('apellido',instance.apellido)
        instance.fechaNacimiento = validated_data.get('fechaNacimiento',instance.fechaNacimiento)
        instance.celular = validated_data.get('celular',instance.celular)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance




