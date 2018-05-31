from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from .serializers import FacturadorSerializer, FacturaElectronicaSerializer
from .models import Facturador, FacturaElectronica


class CreateFacturadorView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Facturador.objects.all()
    serializer_class = FacturadorSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)


class CreateFacturaView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = FacturaElectronica.objects.all()
    serializer_class = FacturaElectronicaSerializer

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content)
