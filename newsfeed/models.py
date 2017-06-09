from django.db import models
from django.utils import timezone

class Product(models.Model):
    sku = models.CharField(max_length=300)
    l1_cat = models.CharField(max_length=300)
    l2_cat = models.CharField(max_length=300)
    l3_cat = models.CharField(max_length=300)
    brand = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    added = models.CharField(max_length=300)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
