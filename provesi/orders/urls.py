from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:order_id>/alistamiento/', views.order_alistamiento_view, name='order-alistamiento'),
    path('orders/', views.OrdersListView.as_view(), name='orders-list'),
]
