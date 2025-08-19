from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Home view - Function Based View
def home(request):
    """
    Home page view
    """
    context = {
        'title': 'Home',
        'message': 'Welcome to our website!',
        'user': 'Laotze',
    }
    return render(request, 'base/home.html', context)

# Writing view - Function Based View (requires login)
def writing(request):
    """
    Writing page view - requires authentication
    """
    context = {
        'title': 'Writing',
        'message': 'Create and manage your content here',
        'user': 'Laotze',
    }
    return render(request, 'base/writing.html', context)

# Alternative: Writing view without login requirement
def writing_public(request):
    """
    Public writing page view - no authentication required
    """
    context = {
        'title': 'Writing',
        'message': 'Create and manage your content here',
        'user': 'Laotze',
    }
    return render(request, 'base/writing.html', context)