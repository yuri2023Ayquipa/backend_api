from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_nacionalidad import Nacionalidad
from ..serializers.serializers_nacionalidad import NacionalidadSerializer

class NacionalidadView(Authentication, APIView):
    permission_classes = (permissions.IsAuthenticated,)    
    serializer_class = NacionalidadSerializer
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    
    def get(self, request):
        tipoDocumento = Nacionalidad.objects.all()
        serializer = NacionalidadSerializer(tipoDocumento, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
