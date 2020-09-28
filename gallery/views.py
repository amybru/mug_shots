from django.shortcuts import render

# Create your views here.

def gallery(request):
    """Render GALLERY Page"""
    context = {
        'gallery_page': 'active'
    }
    return render(request, 'gallery/gallery.html', context)
