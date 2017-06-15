import json
import os

from django.core.management.base import BaseCommand, CommandError

from mysite.settings import BASE_DIR
from newsfeed.models import Product


class Command(BaseCommand):
    help = 'Import producs into database'

    def handle(self, *args, **options):

        # import ipdb; ipdb.set_trace()

        path_to_json = os.path.join(BASE_DIR, 'temporary')

        json_data = open(os.path.join(path_to_json, 'products.json'))
        data = json.load(json_data)
        json_data.close()

        for invariante in range(100):
            entry = data[invariante]
            product = Product.objects.create()
            product.sku = entry['SKU']
            product.l1_category = entry['L1Kategorie']
            product.l2_category = entry['L2Kategorie']
            product.l3_category = entry['L2Kategorie']
            product.product_Brand_Name = entry['productBrandName']
            product.product_Name_de = entry['productName_de']
            product.url = entry['URL']
            product.date_added = entry['Hinzugefügt']
            product.img = entry['Bild']
            product.save()

