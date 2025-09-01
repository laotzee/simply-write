from django.shortcuts import render
from .models import Tag, Prompt

def home(request):
    """Home page view"""
    prompt = Prompt.objects.order_by('?').first()
    context = {
        'prompt': prompt,
    }
    return render(request, 'base/home.html', context)

def writing(request):
    """Writing page view"""
    context = {
    }
    return render(request, 'base/writing.html', context)

def generic_func(request):
    """Generic func for base"""
    context = {
    }
    return render(request, 'base/default.html', context)