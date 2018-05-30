from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateFacturaView, CreateFacturadorView

urlpatterns = {
    url(r'^factura-electronica/$', CreateFacturaView.as_view(), name="create_factura"),
    url(r'^facturador/$', CreateFacturadorView.as_view(), name="create_facturador"),
}

urlpatterns = format_suffix_patterns(urlpatterns)