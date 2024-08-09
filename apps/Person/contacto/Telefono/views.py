from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication


from .models import *
from .serializers import *

# Create your views here.

#crud de Telefono
class TelefonoView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Telefono.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    
    def get(self, request):
        estado_activo = get_object_or_404(Estado, pk=1)
        telefonos = Telefono.objects.filter(id_estado=estado_activo)
        serializer = TelefonoListSerializers(telefonos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new phone record", request_body=TelefonoSerializers, responses={201: TelefonoSerializers})
    def post(self, request):
        serializer = TelefonoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TelefonoDetalleView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TelefonoSerializers
    serializer_classs = TelefonoListSerializers
    queryset = Telefono.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get_telefono(self, pk):
        try:
            return Telefono.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        telefono = self.get_telefono(pk=pk)
        if telefono is None:
            return Response({"status": "fail", "message": f"Telefono with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_classs(telefono)
        return Response({"status": "success", "data": {"telefono": serializer.data}}, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TelefonoSerializers, responses={200: TelefonoSerializers})
    def patch(self, request, pk):
        telefono = self.get_telefono(pk)
        if telefono == None:
            return Response({"status": "fail", "message": f"Telefono with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer =  self.serializer_class(telefono, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"telefono": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, pk):
        telefono = self.get_telefono(pk)
        if telefono is None:
            return Response({"status": "fail", "message": f"Telefono with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener la instancia de Estado con id=2
        estado_inactivo = get_object_or_404(Estado, pk=2)
        
        telefono.id_estado = estado_inactivo
        telefono.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

