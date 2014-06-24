from django.forms import widgets
from django.contrib.auth.models import User
from rest_framework import serializers
# Modules iziapp
from iziapp.models import Customer
from iziapp.models import Invoice
from iziapp.models import InvoiceItem


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','name','email')


class InvoiceItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ('invoice','creation_date')


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    #invoiceitems = serializers.RelatedField(many=True)
	invoiceitems = InvoiceItemSerializer(many=True)

    	class Meta:
        	model = Invoice
        	fields = ('name', 'invoiceitems')
    
