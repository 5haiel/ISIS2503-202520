from django.shortcuts import render
from django.http import JsonResponse, Http404
from .repositories import get_order_with_product_and_location
from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from provesi.auth0backend import getRole
# Create your views here.

class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

@login_required
def orders_list_view(request):
    # permit only Operario de alistamiento
    role = getRole(request)
    if role != "Operario de alistamiento":
        return render(request, "unauthorized.html", {"role": role}, status=403)

    orders = Orders.objects.select_related("producto", "usuario").all()
    return render(request, "orders_list.html", {"orders": orders})

@login_required
def order_detail_view(request, id: int):
    # same role restriction
    role = getRole(request)
    if role != "Operario de alistamiento":
        return render(request, "unauthorized.html", {"role": role}, status=403)

    order = get_order_with_product_and_location(id)
    if not order:
        return JsonResponse({"detail": "Order not found"}, status=404)

    # render a template with the normalized order dict
    return render(request, "order_detail.html", {"order": order})


def order_detail_view_api(request, id: int):
    """Simple JSON-returning view for an order used by the basic API URL."""
    order = get_order_with_product_and_location(id)
    if not order:
        return JsonResponse({"detail": "Order not found"}, status=404)
    return JsonResponse(order)
