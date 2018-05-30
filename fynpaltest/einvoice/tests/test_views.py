from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from rest_framework import status


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.facturaelectronica_data = {}
        self.response = self.client.post(
            reverse('create_factura'),
            self.facturaelectronica_data,
            format="json")

    def test_api_can_create_a_facturaelectronica(self):
        """Test the api has creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)