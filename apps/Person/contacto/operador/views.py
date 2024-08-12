from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication



from .models import Operador
from .serializers import OperadorSerializer

# Create your views here.
class OperadorView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OperadorSerializer
    queryset = Operador.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        operadores = Operador.objects.all()
        serializer = OperadorSerializer(operadores, many=True)
        return Response(serializer.data)
    
