from django.shortcuts import render
from django.http import JsonResponse, Http404
from .repositories import get_order_with_product_and_location
from rest_framework import generics
from .models import Orders
from .serializers import OrdersSerializer
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from provesi.auth0backend import get_role
# Create your views here.

# class OrdersListView(generics.ListAPIView):
#     queryset = Orders.objects.all()
#     serializer_class = OrdersSerializer

@login_required
def orders_list_view(request):
    # permit only Operario de alistamiento
    role = get_role(request)
    if role != "Operario de alistamiento":
        return HttpResponse("Unauthorized User", status=403)

    orders = Orders.objects.select_related("producto", "usuario").all()
    return render(request, "Orders/orders_list.html", {"orders": orders})


# def order_detail_view(request, id: int):
#     try:
#         o = Orders.objects.get_order_with_product_and_location('producto','usuario').get(pk=id)
#     except Orders.DoesNotExist:
#         return JsonResponse({"detail": "Order not found"}, status=404)


@login_required
def order_detail_view(request, id: int):
    # same role restriction
    role = get_role(request)
    if role != "Operario de alistamiento":
        return HttpResponse("Unauthorized User", status=403)

    order = get_order_with_product_and_location(id)
    if not order:
        return JsonResponse({"detail": "Order not found"}, status=404)

    # render a template with the normalized order dict
    return render(request, "Orders/order_detail.html", {"order": order})
