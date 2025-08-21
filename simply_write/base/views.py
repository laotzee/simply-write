from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import Tag, Prompt

# Home view - Function Based View
def home(request):
    """
    Home page view
    """
    prompt = Prompt.objects.order_by('?').first()
    context = {
        'title': 'Home',
        'message': 'Welcome to our website!',
        'user': 'Laotze',
        'prompt': prompt,
    }
    return render(request, 'base/home.html', context)

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

def generic_func(request):
    """
    Generic func for base
    """
    context = {

    }
    return render(request, 'base/default.html', context)