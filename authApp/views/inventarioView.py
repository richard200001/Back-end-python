from django.http.response import Http404
from rest_framework import  status, views
from rest_framework.response import Response

from authApp.models.inventario import Inventario
from authApp.serializers.inventarioSerializer import InventarioSerializer

class InventarioView(views.APIView):
    def get_object(self,id):
        try:
            return Inventario.objects.get(pk=id)
        except Inventario.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        invent=Inventario.objects.all()
        serializer=InventarioSerializer(invent,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer=InventarioSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    