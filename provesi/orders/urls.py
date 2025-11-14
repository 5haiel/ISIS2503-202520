from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.OrdersListView.as_view(), name='orders-list'),
    path('api/<int:id>/', views.order_detail_view_api, name='order-detail-api'),

    path('', views.orders_list_view, name='orders-list-ui'),
    path('<int:id>/', views.order_detail_view, name='order-detail-ui'),
    path("<int:order_id>/edit/", views.update_quantity, name="edit_order"),
]
