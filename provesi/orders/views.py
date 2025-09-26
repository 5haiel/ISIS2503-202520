from django.shortcuts import render
from django.http import JsonResponse, Http404
from .services.service import fetch_order_for_alistamiento
from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer
# Create your views here.

class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

def order_alistamiento_view(request, order_id):
    data = fetch_order_for_alistamiento(order_id, request=request)
    if not data:
        raise Http404("Order not found")
    return JsonResponse(data, safe=False)
