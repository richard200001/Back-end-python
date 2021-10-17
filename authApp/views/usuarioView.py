from django.conf import settings
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated

from authApp.models.usuario import Usuario
from django.http import Http404
from authApp.serializers.usuarioSerializer import UsuarioSerializer


class UsuarioView(views.APIView):
    
    
    def get_user(self, id):
        try:
            return Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            raise Http404

    def put(self, request, *args, **kwargs):
        usuario = self.get_user(kwargs['id'])
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        usuario = self.get_user(kwargs['id'])
        usuario.delete()
        return Response(status=status.HTTP_200_OK)