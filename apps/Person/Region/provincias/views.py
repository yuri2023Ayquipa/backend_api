from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication

from ..departamentos.models import Departamento
from .serializers import DepartamentoDetailSerializer

# Create your views here.

class DepartamentoDetailView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request, id_departamento):
        try:
            departamento = Departamento.objects.get(id=id_departamento)
        except Departamento.DoesNotExist:
            return Response({"error": "Departamento no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartamentoDetailSerializer(departamento)
        return Response(serializer.data, status=status.HTTP_200_OK)