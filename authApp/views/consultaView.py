from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authApp.models.consulta import Consulta
from authApp.models.usuario import Usuario
from authApp.models.inventario import Inventario
from django.http import Http404

from authApp.serializers.consultaSerializer import ConsultaSerializer

class ConsultaView(views.APIView):
    def get_user(self, id):
        try:
            return Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            raise Http404
    def get_product(self, id):
        try:
            return Inventario.objects.get(pk=id)
        except Inventario.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        consulta = Consulta.objects.all()
        serializer = ConsultaSerializer(consulta, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        responseUser = self.get_user(request.data['idUsu'])
        print(responseUser)
        responseProduct = self.get_product(request.data['idInv'])
        print(responseProduct)
        Consulta.objects.create( idUsu=responseUser, idInv=responseProduct)
        return Response({"message": "Se ha creado la consulta"}, status=status.HTTP_201_CREATED)
