from rest_framework import serializers

from ..models.models_tipo_documento import TipoDocumento

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDocumento
        fields = ['id', 'id_sunat', 'denominacion']