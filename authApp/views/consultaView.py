from django.conf import settings
from rest_framework import status, views
from rest_framework import response
from rest_framework.response import Response

from authApp.models.consulta import Consulta
from authApp.serializers.consultaSerializer import ConsultaSerializer

class consultaView(views.APIView):

    def get(self, request, *args, **kwargs):
        consult=Consulta.objects.all()
        serializer=ConsultaSerializer(consult,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    