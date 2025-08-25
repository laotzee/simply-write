from django.urls import path
from . import views

urlpatterns = [
    path('prompt/', views.get_prompt, name='prompt'),
]


