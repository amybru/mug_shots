from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """A view to show all products in the database, including the option to sort and search"""
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category_name_in=categories)
            categories = Category.objects.filter(name_in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter search criteria to search")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'shop_page': 'active'
    }
    return render(request, 'products/products.html', context)


def one_product(request, product_id):
    """A view to show one product in the database"""

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
        'shop_page': 'active'
    }

    return render(request, 'products/one_product.html', context)

