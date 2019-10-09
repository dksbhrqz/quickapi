from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
from .models import Client, Bill, Product, BillProduct

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('last_name')
    serializer_class = ClientSerializer

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillProductViewSet(viewsets.ModelViewSet):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer