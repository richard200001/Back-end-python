from django.conf import settings
from rest_framework import status, views, generics
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from authApp.models.usuario import Usuario
from django.http import Http404
from authApp.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioGetView(generics.RetrieveAPIView):
    
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_user(self, id):
        try:
            return Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        if valid_data['user_id'] != kwargs['id']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        usuario = self.get_user(kwargs['id'])
        serializer = UsuarioSerializer(usuario)

        return Response( serializer.data, status=status.HTTP_200_OK)