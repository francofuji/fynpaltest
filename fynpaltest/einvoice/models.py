import uuid
from django.db import models


class Facturador(models.Model):
	"""docstring for Facturador"""
	rut = models.CharField()
	razon_social = models.CharField()

	def __init__(self, arg):
		super(Facturador, self).__init__()
		self.arg = arg
		


class FacturaElectronica(models.Model):
	"""docstring for FacturaElectronica"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	dte_version = models.CharField()
	document_id = models.CharField()
	folio = models.IntegerField()
	fecha_emision = models.DateField()
	emisor = models.ForeingKey(Facturador, relation_name = "emitidas")
	receptor = models.ForeingKey(Facturador, relation_name = "recibidas")
	tasa_iva = models.DecimalField(max_digits=5, decimal_places=2)
	monto_neto = models.IntegerField()
	monto_iva = models.IntegerField()
	monto_total = models.IntegerField()
	extra_data = models.CharField()

	def _monto_iva(self):
		"Calculate monto_iva"
		return self.tasa_iva * self.monto_neto