from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_departamento import Departamento
from ..serializers.serializers_departamento import DepartamentoSerializer

# Create your views here.
class DepartamentoView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        departamento = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)