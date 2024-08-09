from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.sessions.models import Session

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny
from .serializers import UserTokenSerializer, loginSerializer
from .models import Users, Estado

from django.shortcuts import get_object_or_404

class Login(ObtainAuthToken):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        # Obtener el estado activo usando el pk (1 en este caso)
        estado_activo = get_object_or_404(Estado, pk=1)
        
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        if login_serializer.is_valid(raise_exception=True):
            # Obtener el usuario desde los datos validados del serializador
            user = login_serializer.validated_data['user']
            
            # Verificar si el usuario está activo (booleano)
            if user.is_active == estado_activo:
                # Eliminar el token existente (si existe)
                Token.objects.filter(user=user).delete()
                
                # Crear un nuevo token
                token = Token.objects.create(user=user)
                user_serializer = loginSerializer(user)  # Usa el serializador correcto para el usuario
                
                return Response({
                    'token': token.key,
                    'user': user_serializer.data,
                    'message': 'Inicio de sesión exitoso.'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Este usuario no está activo.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=status.HTTP_400_BAD_REQUEST)
        #return Response({'mesanje':'Hola desde response.'}, status=status.HTTP_200_OK)

class Logout(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token_key = request.GET.get('token')  # Obtener el token de los parámetros de la URL
            token = Token.objects.filter(key=token_key).first()

            if token:
                user = token.user

                # Filtrar las sesiones que aún no han expirado
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())

                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()

                token.delete()
                session_message = 'Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'

                return Response({'token_message': token_message, 'session_message': session_message}, status=status.HTTP_200_OK)

            return Response({'error': 'No se ha encontrado un usuario'}, status=status.HTTP_400_BAD_REQUEST)   
        except:
            return Response({'error':'no se encontro el token'}, status=status.HTTP_409_CONFLICT)