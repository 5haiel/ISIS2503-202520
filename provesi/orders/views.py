from django.shortcuts import render
from django.http import JsonResponse, Http404
from .repositories import get_order_with_product_and_location
from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer
# Create your views here.

class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

def order_detail_view(request, id: int):
    data = get_order_with_product_and_location(id)
    if data is None:
        return JsonResponse({"detail": "Order not found"}, status=404)
    return JsonResponse(data, status=200)
