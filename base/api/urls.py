from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.get_prompt, name=''),
    path('v1/prompts/', views.get_prompt, name='prompts'),
]


