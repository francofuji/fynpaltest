import uuid
from django.db import models


class Facturador(models.Model):
	"""docstring for Facturador"""

	rut = models.CharField(max_length = 10)
	razon_social = models.CharField(max_length = 50)


class FacturaElectronica(models.Model):
	"""docstring for FacturaElectronica"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	dte_version = models.CharField(max_length = 4)
	document_id = models.CharField(max_length = 10)
	folio = models.PositiveIntegerField()
	fecha_emision = models.DateField()
	emisor = models.ForeignKey(Facturador, related_name = "emitidas", on_delete = models.CASCADE)
	receptor = models.ForeignKey(Facturador, related_name = "recibidas", on_delete = models.CASCADE)
	tasa_iva = models.DecimalField(max_digits=5, decimal_places=2)
	monto_neto = models.IntegerField()
	extra_data = models.CharField(max_length = 50)

