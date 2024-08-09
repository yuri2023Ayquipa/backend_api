from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication

from .models import Genero
from .serializers import GeneroSerializer

# Create your views here.
class GeneroView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GeneroSerializer
    queryset = Genero.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)