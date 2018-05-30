from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(), name='home', template_name = "home.html"),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('einvoice.urls')) # Add this line
]
