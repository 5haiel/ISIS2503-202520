from django.urls import path
from . import views

urlpatterns = [
    # API endpoints (keep if you want the DRF ones)
    path('api/', views.OrdersListView.as_view(), name='orders-list'),
    path('api/<int:id>/', views.order_detail_view_api, name='order-detail-api'),

    # Template UI endpoints (for the role-protected UI)
    path('', views.orders_list_view, name='orders-list-ui'),
    path('<int:id>/', views.order_detail_view, name='order-detail-ui'),
]
