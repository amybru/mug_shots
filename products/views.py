from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """A view to show all products in the database, including the option to sort and search"""

    products = Product.objects.all()

    context = {
        'products': products,
        'all_products': 'active'
    }
    return render(request, 'products/products.html', context)

