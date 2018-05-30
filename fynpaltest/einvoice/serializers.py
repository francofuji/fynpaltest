from rest_framework import serializers
from .models import Facturador, FacturaElectronica


class FacturadorSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = Facturador
        fields = ('id', 'rut', 'razon_social')

class FacturaElectronicaSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance."""

    emisor_rut = serializers.SerializerMethodField()
    emisor_razon_social = serializers.SerializerMethodField()
    receptor_rut = serializers.SerializerMethodField()
    receptor_razon_social = serializers.SerializerMethodField()

    def get_emisor_rut(self, obj):
        return obj.emisor.rut

    def get_emisor_razon_social(self, obj):
        return obj.emisor.razon_social

    def get_receptor_rut(self, obj):
        return obj.receptor.rut

    def get_receptor_razon_social(self, obj):
        return obj.receptor.razon_social



    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = FacturaElectronica
        fields = ('id', 'dte_version', 'document_id', 'folio', 'fecha_emision', 'emisor', 'receptor', 'emisor_rut', 'emisor_razon_social',
        	'receptor_rut', 'receptor_razon_social', 'tasa_iva', 'monto_neto', 'extra_data')
        read_only = ()
