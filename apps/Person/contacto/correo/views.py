from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication


from .models import Correo, Estado
from .serializers import CorreoSerializers, CorreoPostSerializers

# Create your views here.
class CorreoView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Correo.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )

    def get(self, request):
        estado_activo = get_object_or_404(Estado, pk=1)
        correos = Correo.objects.filter(id_estado=estado_activo)
        serializer = CorreoSerializers(correos, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Create a new correo record", request_body=CorreoPostSerializers, responses={201: CorreoPostSerializers})
    def post(self, request):
        serializer = CorreoPostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CorreoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CorreoPostSerializers
    serializer_classs = CorreoSerializers

    queryset = Correo.objects.all()

    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get_correo(self, pk):
        try:
            return Correo.objects.get(pk=pk)
        except:
            return None
    
    def get(self, request, pk):
        correo = self.get_correo(pk=pk)
        if correo is None:
            return Response({"status": "fail", "message": f"Correo with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_classs(correo)
        return Response({"status": "success", "data": {"correo": serializer.data}}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=CorreoPostSerializers, responses={200: CorreoPostSerializers})
    def patch(self, request, pk):
        correo = self.get_correo(pk)
        if correo is None:  
            return Response({"status": "fail", "message": f"correo with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(correo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updateAt'] = datetime.now()
            serializer.save()
            return Response({"status": "succes", "data": {"correo": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        correo = self.get_correo(pk)
        if correo is None:
            return Response({"status": "fail", "message": f"correo with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener la instancia de Estado con id=2
        estado_inactivo = get_object_or_404(Estado, pk=2)
        # Actualizar el estado del correo a inactivo
        correo.id_estado = estado_inactivo
        correo.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

