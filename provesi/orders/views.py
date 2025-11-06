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

def order_alistamiento_view(request, order_id):
    data = get_order_with_product_and_location(order_id, request=request)
    if not data:
        raise Http404("Order not found")
    return JsonResponse(data, safe=False)

