from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ClientSerializer, BillSerializer, ProductSerializer, BillProductSerializer
from .models import Client, Bill, Product, BillProduct

import csv
from django.http import HttpResponse

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

def export_clients_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_simple_write.csv"'
    client_list = []
    client_list = Client.objects.raw('SELECT * FROM clients')
    writer = csv.writer(response)
    writer.writerow(['ID', 'first_name', 'last_name', 'email'])
    for k in client_list.iterator():
        writer.writerow([k.pk, k.first_name, k.last_name, k.email])

    return response