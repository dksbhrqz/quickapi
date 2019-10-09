from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)

    class Meta:
        db_table = 'clients'

class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60)
    nit = models.CharField(max_length=60)
    code = models.CharField(max_length=60)

    class Meta:
        db_table = 'bills'

class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    class Meta:
        db_table = 'products'

class BillProduct(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'bills_products'
