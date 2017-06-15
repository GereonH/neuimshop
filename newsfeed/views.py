from django.shortcuts import render

from django.views.generic.list import ListView
from django.utils import timezone

from newsfeed.models import Product


class ProductListView(ListView):

    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context
#
# def post_list(request):
#     return render(request, 'newsfeed/product_list.html', {})
