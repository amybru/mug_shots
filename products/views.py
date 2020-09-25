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

def one_product(request, product_id):
    """A view to show one product in the database"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'all_products': 'active'
    }

    return render(request, 'products/products.html', context)

