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

    class Meta:
        """Meta class to map serializer's fields with the model fields."""

        model = FacturaElectronica
        fields = ('id', 'dte_version', 'document_id', 'folio', 'fecha_emision', 'emisor_rut', 'emisor_name',
        	'receptor_rut', 'receptor_name', 'tasa_iva', 'monto_neto', 'extra_data')
