from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('writing/', views.writing, name='writing'),
    path('default/', views.generic_func, name='default'),
]