from rest_framework import serializers
from authApp.models.usuario import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Usuario
        fields = ['id','username','password', 'nombre', 'apellido','fechaNacimiento','celular','email','rol','estado','fechaRegistro']