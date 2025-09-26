from django.shortcuts import render
from django.http import JsonResponse, Http404
from .services import fetch_order_for_alistamiento

# Create your views here.
def order_alistamiento_view(request, order_id):
    data = fetch_order_for_alistamiento(order_id, request=request)
    if not data:
        raise Http404("Order not found")
    return JsonResponse(data, safe=False)
