from django.db import models
from django.utils import timezone


class Product(models.Model):
    sku = models.CharField(max_length=300)
    l1_category = models.CharField(max_length=300)
    l2_category = models.CharField(max_length=300)
    l3_category = models.CharField(max_length=300)
    product_Brand_Name = models.CharField(max_length=300)
    product_Name_de = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    date_added = models.CharField(max_length=300)
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.product_Name_de
