from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions

from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_estado import Estado
from ..serializers.serializers_estado import EstadoSerializer

# Create your views here
class EstadoView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EstadoSerializer
    queryset = Estado.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        estado = Estado.objects.all()
        serializer = EstadoSerializer(estado, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
