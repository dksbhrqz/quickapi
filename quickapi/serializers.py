from rest_framework import serializers

from .models import Client, Bill, Product, BillProduct

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class BillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BillProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BillProduct
        fields = '__all__'