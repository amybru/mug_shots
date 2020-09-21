from django.shortcuts import render

# Create your views here.


def index(request):
    """Render Index page"""
    context = {
        'home_page': 'active'
    }
    return render(request, 'home/index.html', context)
