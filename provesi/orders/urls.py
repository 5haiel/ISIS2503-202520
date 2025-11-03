from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrdersListView.as_view(), name='orders-list'),          # GET /orders/
    path('<int:order_id>/', views.order_detail_view, name='order-detail'), # GET /orders/1/
]
