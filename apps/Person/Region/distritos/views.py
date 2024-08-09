from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication

from ..provincias.models import Provincia
from .serializers import ProvinciaDetailSerializer

# Create your views here.
class ProvinciaDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request, id_provincia):
        try:
            provincia = Provincia.objects.get(id=id_provincia)
        except Provincia.DoesNotExist:
            return Response({"error": "Provincia no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProvinciaDetailSerializer(provincia)
        return Response(serializer.data, status=status.HTTP_200_OK)