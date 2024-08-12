from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

from .models import Users, Estado
from .serializers import UserSerializer 
from apps.User.authenticacion_mixins import Authentication

# Create your views here.
estado_activo = get_object_or_404(Estado, pk=1)
@method_decorator(csrf_exempt, name='dispatch')
class UserView(Authentication, APIView):
    queryset = Users.objects.all()

    def get(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        usuarios = Users.objects.filter(is_active=estado_activo)
        serializer = UserSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new user record", request_body=UserSerializer, responses={201: UserSerializer})
    def post(self, request):
        permission_classes = (permissions.AllowAny,)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get_user(self, pk):
        try:
            return get_object_or_404(Users, pk=pk, is_active=estado_activo)
        except Users.DoesNotExist:
            raise None
        
    def get(self, request, pk):
        user = self.get_user(pk)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(request_body=UserSerializer, responses={200: UserSerializer})
    def patch(self, request, pk):
        user = self.get_user(pk)
        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in serializer.validated_data:
                user.set_password(serializer.validated_data['password'])
                del serializer.validated_data['password']
            serializer.validated_data["updatedAt"] = datetime.now()
            for attr, value in serializer.validated_data.items():
                setattr(user, attr, value)
            user.save()
            return Response({"status": "success", "data": {"user": serializer.data}}, status=status.HTTP_200_OK)
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
#class LoginView(APIView):
#    @swagger_auto_schema(
#        request_body=UserLoginSerializer,
#        responses={
#            200: 'Token generado exitosamente',
#            400: 'Credenciales inválidas'
#        }
#    )    
#    def post(self, request):
#        
#        username = request.data.get('username')
#        password = request.data.get('password')
#        user = authenticate(username=username, password=password)
#
#        if user is not None:
#            # Elimina los tokens expirados
#            expired_tokens = ExpiringToken.objects.filter(user=user, created__lt=timezone.now() - settings.TOKEN_EXPIRATION_DELTA)
#            print("Expired tokens:", expired_tokens)
#
#            # Crea un Token o actualiza el existente
#            token, created = ExpiringToken.objects.get_or_create(user=user)
#
#            if not created:
#                # Actualiza la fecha de creación del token si ya existe
#                token.created = timezone.now()
#                token.save()
#
#            return Response({'token': token.key}, status=status.HTTP_200_OK)
#        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)
    
    #455a0a238b37f76e33dea89dd8780835d3dff0f4
    
#class ProtectedView(APIView):
#    authentication_classes = [TokenAuthentication]
#    permission_classes = [IsAuthenticated]
#    
#    def get(self, request):
#        return Response({"message": "This is a protected view"}, status=200)

