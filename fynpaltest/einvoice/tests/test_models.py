from datetime import datetime
from django.test import TestCase
from einvoice.models import Facturador, FacturaElectronica


class ModelTestCase(TestCase):
    """This class defines the test suite for the FacturaElectronica model."""

    def setUp(self):
        """Define the test client and other test variables."""

        self.emisor = Facturador(rut = "22222222-2", razon_social = "razon social emisor")
        self.emisor.save()
        self.receptor = Facturador(rut = "44444444-2", razon_social = "razon social receptor")
        self.receptor.save()

        self.factura = FacturaElectronica()
        self.factura.dte_version = "1.0"
        self.factura.document_id = "F1387T33"
        self.factura.folio = 1387
        self.factura.fecha_emision = datetime.now()
        self.factura.emisor = self.emisor
        self.factura.receptor = self.receptor
        self.factura.tasa_iva = 17
        self.factura.monto_neto = 0
        self.factura.extra_data = ""
        self.factura.save()



    def test_model_can_create_facturador(self):
        """Test the Facturador model records counts."""
        
        self.assertEqual(2, Facturador.objects.count())

    def test_model_can_create_factura(self):
        """Test the FacturaElectronica model records counts."""
        
        self.assertEqual(1, FacturaElectronica.objects.count())


    def test_factura_emisor(self):
        """"Test FacturaElectronica emisor field"""

        self.assertEqual(self.emisor, FacturaElectronica.objects.all()[0].emisor)
