from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_tipo_contribuyente import TipoContribuyente
from ..serializers.serializers_tipo_contribuyente import TipoContribuyenteSerializer

# Create your views here.
class TipoContribuyenteView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serialiser = TipoContribuyenteSerializer
    queryset = TipoContribuyente.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        tipo_contribuyente = self.queryset.all()
        serializer = self.serialiser(tipo_contribuyente, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)