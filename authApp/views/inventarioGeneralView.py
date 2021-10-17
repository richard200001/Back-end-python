from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.models.inventario import Inventario
from django.http import Http404
from authApp.serializers.inventarioSerializer import InventarioSerializer

class InventarioGeneralView(views.APIView):
    

    def get(self, request, *args, **kwargs):
            producto = Inventario.objects.all()
            serializer = InventarioSerializer(producto, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = InventarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)