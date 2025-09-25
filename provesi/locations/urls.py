from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('locations/', views.locationlist),
    path('locationcreate/', csrf_exempt(views.location_create), name='locationCreate'),
    path('location/<str:product_name>/', views.location_by_product, name='locationByProduct'),
]