from rest_framework import serializers

from ..models.models_person_natural import PersonaNatural
from ..models.models_genero import Genero
from  ..models.models_person import Persona

from .serializers_person import PersonaSerializer, PersonaListSerializer

class PersonaNaturalGetSerializer(serializers.ModelSerializer):
    id_persona = PersonaListSerializer()

    class Meta:
        model = PersonaNatural
        
    def to_representation(self, instance):
        return {
            'id_persona': PersonaListSerializer(instance.id_persona).data,
            'id': instance.id,
            'primer_nombre': instance.primer_nombre,
            'segundo_nombre': instance.segundo_nombre,
            'apellido_paterno': instance.apellido_paterno,
            'apellido_materno': instance.apellido_materno,
            'fecha_nacimiento': instance.fecha_nacimiento.strftime('%Y-%m-%d'),
            'id_genero': instance.id_genero.abreviatura
        }
class PersonaNaturalPostSerializer(serializers.ModelSerializer):
    id_persona = PersonaSerializer()
    id_genero = serializers.PrimaryKeyRelatedField(queryset=Genero.objects.all())

    class Meta:
        model = PersonaNatural
        fields = [
            'id_persona',
            'primer_nombre',
            'segundo_nombre',
            'apellido_paterno',
            'apellido_materno',
            'fecha_nacimiento',
            'id_genero'
        ]
    def create(self, validated_data):
        # Extraer los datos de Persona
        persona_data = validated_data.pop('id_persona')
        # Crear la instancia de Persona
        persona = Persona.objects.create(**persona_data)
        # Crear la instancia de PersonaNatural usando la instancia de Persona
        persona_natural = PersonaNatural.objects.create(id_persona=persona, **validated_data)
        return persona_natural
