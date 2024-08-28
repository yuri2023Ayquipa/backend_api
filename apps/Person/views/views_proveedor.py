from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_list_or_404
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_proveedor import Proveedor

from ..serializers.serializers_proveedor import ProveedorGetSerializer, ProveedorPostSerializer

class ProveedorView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Proveedor.objects.all()
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        proveedores = self.queryset.all()
        serializer = ProveedorGetSerializer(proveedores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new proveedor record", request_body=ProveedorPostSerializer, responses={201: ProveedorPostSerializer})
    def post(self, request):
        serializer = ProveedorPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProveedorDetailView(Authentication,APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProveedorPostSerializer
    queryset = Proveedor.objects.all()
    authentication_classes = [TokenAuthentication]
    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get_proveedor(self, request, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            return None
    
    def get(self, request, pk):
        proveedor = self.get_proveedor(pk=pk)
        if proveedor is None:
            return Response({"status": "fail", "message": f"Proveedor with Id: {pk} not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = ProveedorGetSerializer(proveedor)
        return Response({"status": "succes", "data": {"proveedor": serializer.data}}, status=status.HTTP_200_OK)