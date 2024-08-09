from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from datetime import datetime
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication

from .models import *
from .serializers import DireccionSerializer, DireccionListSerializer

# Create your views here.

class DireccionView(APIView):
    serializer_class = DireccionListSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        estado_inactivo = get_object_or_404(Estado, pk=1)
        direcciones = Direccion.objects.filter(id_estado=estado_inactivo)
        serializer = DireccionListSerializer(direcciones, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new phone record", request_body=DireccionSerializer, responses={201: DireccionSerializer})
    def post(self, request):
        serializer = DireccionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DireccionDetalleView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = DireccionSerializer
    serializer_classs = DireccionListSerializer
    queryset = Direccion.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )

    def get_direccion(self, pk):
        try:
            return Direccion.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        direccion = self.get_direccion(pk=pk)
        if direccion is None:
            return Response({"status": "fail", "message": f"Direccion with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_classs(direccion)
        return Response({"status": "success", "data": {"direccion": serializer.data}}, status=status.HTTP_200_OK)


    @swagger_auto_schema(request_body=DireccionSerializer, responses={200: DireccionSerializer})
    def patch(self, request, pk):
        direccion = self.get_direccion(pk)
        if direccion == None:
            return Response({"status": "fail", "message": f"Telefono with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer =  self.serializer_class(direccion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "data": {"direccion": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        direccion = self.get_direccion(pk)
        if direccion is None:
            return Response({"status": "fail", "message": f"Telefono with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener la instancia de Estado con id=2
        estado_inactivo = get_object_or_404(Estado, pk=2)
        
        direccion.id_estado = estado_inactivo
        direccion.save()
        return Response(status=status.HTTP_204_NO_CONTENT)