from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status

from einvoice.models import Facturador, FacturaElectronica

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.emisor_data = {"rut": "22222222-2", "razon_social": "razon social emisor"}
        self.receptor_data = {"rut": "44444444-4", "razon_social": "razon social receptor"}

        self.response_emisor = self.client.post(
            reverse('einvoice:create_facturador'),
            self.emisor_data,
            format="json")

        self.response_receptor = self.client.post(
            reverse('einvoice:create_facturador'),
            self.receptor_data,
            format="json")


        self.facturaelectronica_data = {
            "dte_version": "1.0",
            "document_id": "FT12345",
            "folio": 12345,
            "fecha_emision": datetime.now().strftime("%Y-%m-%d"),
            "emisor": int(self.response_emisor.data['id']),
            "receptor": int(self.response_receptor.data['id']),
            "tasa_iva": 17,
            "monto_neto": 18,
            "extra_data": "empty"
        }

        self.response_factura = self.client.post(
            reverse('einvoice:create_factura'),
            self.facturaelectronica_data,
            format="json")

    def test_api_can_create_emisor(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_emisor.status_code, status.HTTP_201_CREATED)

    def test_api_can_create_receptor(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_receptor.status_code, status.HTTP_201_CREATED)


    def test_api_can_create_facturaelectronica(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response_factura.status_code, status.HTTP_201_CREATED)
