from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from datetime import datetime
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_person import Persona
from ..models.models_estado import Estado

from ..serializers.serializers_person import PersonaGetSerializer, PersonaSerializer

class PersonaView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Persona.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    
    def get(self, request):
        estado_activo = get_object_or_404(Estado, pk=1)
        personas = Persona.objects.filter(id_estado=estado_activo)
        serializer = PersonaGetSerializer(personas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new persona record", request_body=PersonaSerializer, responses={201: PersonaSerializer})
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaDetailView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonaSerializer
    queryset = Persona.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    
    def get_persona(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            return None
        
    def get(self, request, pk):
        persona = self.get_persona(pk=pk)
        if persona is None:
            return Response({"status": "fail", "message": f"Persona with Id: {pk} not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaGetSerializer(persona)
        return Response({"status": "succes", "data": {"persona": serializer.data}}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=PersonaSerializer, responses={200: PersonaSerializer})
    def patch(self, request, pk):
        persona = self.get_persona(pk)
        if persona is None:
            return Response({"status": "fail", "message": f"Persona with Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(persona, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data["upsateAt"] =datetime.now()
            serializer.save()
            return Response({"status": "succes", "data": {"persona": serializer.data}}, status=status.HTTP_200_OK)
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        persona = self.get_persona(pk)
        if persona is None:
            return Response({"status": "fail", "message": f"Persona wirh Id: {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        
        estado_inactivo = get_object_or_404(Estado,pk=2)

        persona.id_estado = estado_inactivo
        persona.save()
        return Response(status=status.HTTP_204_NO_CONTENT)