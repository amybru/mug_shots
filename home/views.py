from django.shortcuts import render

"""
Render Index page
"""


def index(request):

    context = {
        'home_page': 'active'
    }
    return render(request, 'home/index.html', context)
