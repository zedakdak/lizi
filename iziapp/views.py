from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
# Modules Izi
from iziapp.models import Customer, Invoice, InvoiceItem
from iziapp.serializers import CustomerSerializer, InvoiceSerializer, InvoiceItemSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    """permission_classes = (permissions.IsAuthenticatedOrReadOnly,)"""
    permission_classes = (permissions.AllowAny,)

    def list(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        # Reponse.content_type = "text/html"
        return Response(serializer.data)


class InvoiceViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class InvoiceItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



