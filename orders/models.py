from django.db import models


# Create your models here.
class Order (models.Model):
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField()
    creation_date = models.DateField(blank=True)
    product_id = models.TextField()
    payment_option = models.CharField(max_length=50)
    number_of_packets = models.IntegerField()
    weight = models.IntegerField()
    inventory_warehouse = models.CharField(max_length=200)
    transportation_vender = models.CharField(max_length=200)
    delivery_order_id = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
