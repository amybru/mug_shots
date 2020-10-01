from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """A view that will render the contents of the shopping bag"""
    context = {
        'cart': 'active'
    }
    return render(request, 'bag/bag.html', context)
