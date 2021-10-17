from django.conf import settings
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated


from authApp.models.inventario import Inventario
from django.http import Http404

from authApp.serializers.inventarioSerializer import InventarioSerializer

class InventarioView(views.APIView):
    def get_producto(self, id):
        try:
            return Inventario.objects.get(pk=id)
        except Inventario.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        producto = self.get_producto(kwargs['id'])
        serializer = InventarioSerializer(producto)  
        return Response(serializer.data)


    def put(self, request, *args, **kwargs):
        producto = self.get_producto(kwargs['id'])
        serializer = InventarioSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        producto = self.get_producto(kwargs['id'])
        producto.delete()
        return Response(status=status.HTTP_200_OK)