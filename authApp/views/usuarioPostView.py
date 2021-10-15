from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authApp.serializers.usuarioSerializer import UsuarioSerializer

class UsuarioPostView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        tokenData = { "username":request.data["username"], 
                      "password":request.data["password"] }
        token_Serializer = TokenObtainPairSerializer(data=tokenData)
        token_Serializer.is_valid(raise_exception=True)
        return Response(token_Serializer.validated_data, status=status.HTTP_201_CREATED)