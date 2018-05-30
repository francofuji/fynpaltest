from rest_framework import generics
from .serializers import FacturadorSerializer, FacturaElectronicaSerializer
from .models import Facturador, FacturaElectronica


class CreateFacturadorView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Facturador.objects.all()
    serializer_class = FacturadorSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class CreateFacturaView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = FacturaElectronica.objects.all()
    serializer_class = FacturaElectronicaSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()