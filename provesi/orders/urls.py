from django.urls import path
from . import views

urlpatterns = [
    path('orders/<int:order_id>/', views.order_detail_view, name='order-detail'),
    path('orders/', views.OrdersListView.as_view(), name='orders-list'),
]
