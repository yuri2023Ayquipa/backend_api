from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_origen_entidad import OrigenEntidad
from ..serializers.serializers_origen_entidad import OrigenEntidadSerializer

class OrigenEntidadView(Authentication, APIView):
    permission_classes = (permissions.IsAuthenticated,)    
    serializer_class = OrigenEntidadSerializer
    queryset = OrigenEntidad.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        tipoDocumento = OrigenEntidad.objects.all()
        serializer = OrigenEntidadSerializer(tipoDocumento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
