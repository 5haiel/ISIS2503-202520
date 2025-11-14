"""provesi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse
from django.urls import path, include
from . import views

def home(request):
    return HttpResponse("<h1>Bienvenido a la API de Provesi 🚀</h1><p>Visita <a href='/orders/'>/orders/</a> para ver las órdenes.</p>")

urlpatterns = [
    path('', home),  # 👈 Página principal
    path('health/', views.health_check, name = 'health'),
    path('orders/', include('orders.urls')),
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
]
