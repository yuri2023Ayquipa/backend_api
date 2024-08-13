from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_person_natural import PersonaNatural
from ..serializers.serializers_person_natural import PersonaNaturalSerializer

# Create your views here.
class PersonaNaturalView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonaNaturalSerializer
    queryset = PersonaNatural.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        persona_natural = PersonaNatural.objects.all()
        serializer = PersonaNaturalSerializer(persona_natural, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_description="Create a new phone record", request_body=PersonaNaturalSerializer, responses={201: PersonaNaturalSerializer})
    def post(self, request):
        serializer = PersonaNaturalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonaNaturalDetailView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonaNaturalSerializer
    queryset = PersonaNatural.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get_persona(self, pk):
        try:
            return PersonaNatural.objects.get(pk=pk)
        except:
            return None
    
    def get(self, request, pk):
        personaNatural = self.get_persona(pk=pk)
        if personaNatural is None:
            return Response({"status": "fail", "message": f"Persona Natural with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaNaturalSerializer(personaNatural)
        return Response({"status": "succes", "data": {"persona Natural": serializer.data}}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=PersonaNaturalSerializer, responses={200: PersonaNaturalSerializer})
    def patch(self, request, pk):
        personaNatural = self.get_persona(pk)
        if personaNatural == None:
            return Response({"status": "fail", "message": f"Persona Juridica with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaNaturalSerializer(personaNatural, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "succes", "data": {"personaNatural": serializer.data}})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    