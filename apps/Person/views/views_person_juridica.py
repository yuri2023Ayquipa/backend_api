from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from apps.User.authenticacion_mixins import Authentication

from ..models.models_person_juridica import PersonaJuridica
from ..serializers.serializers_person_juridica import PersonaJuridicaSerializer

# Create your views here.
class PersonaJuridicaView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonaJuridicaSerializer
    queryset = PersonaJuridica.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get(self, request):
        personaJuridica = PersonaJuridica.objects.all()
        serializer = PersonaJuridicaSerializer(personaJuridica, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="Create a new Persona Juridica record", request_body=PersonaJuridicaSerializer, response={201: PersonaJuridicaSerializer})
    def post(self, request):
        serializer = PersonaJuridicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PersnaJuridicaDetailView(Authentication, APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PersonaJuridicaSerializer
    queryset = PersonaJuridica.objects.all()
    authentication_classes = [TokenAuthentication]

    @swagger_auto_schema(
        security=[{'Token': []}]
    )
    def get_persona(self, pk):
        try:
            return PersonaJuridica.objects.get(pk=pk)
        except:
            return None
        
    def get(self, request, pk):
        personaJuridica = self.get_persona(pk=pk)
        if personaJuridica is None:
            return Response({"status": "fail", "message": f"Persona Juridica with Id : {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaJuridicaSerializer(personaJuridica)
        return Response({"status": "succes", "data": {"persona Juridica": serializer.data}}, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=PersonaJuridicaSerializer, responses={200: PersonaJuridicaSerializer})
    def patch(self, request, pk):
        personaJuridica = self.get_persona(pk)
        if personaJuridica is None:
            return Response({"status": "fail", "message": f"Persona Juridica with Id:{pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PersonaJuridicaSerializer(personaJuridica, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "succes", "data": {"persona Juridica": serializer.data}})
        return Response({"status": "fail", "message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

