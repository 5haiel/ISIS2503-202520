from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import OrdersViewSet

router = DefaultRouter()
router.register(r'orders', OrdersViewSet, basename='orders')

urlpatterns = router.urls