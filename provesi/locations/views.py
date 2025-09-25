from django.shortcuts import render
from .forms import LocationForms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_locations import create_location, get_location
from .models import Location
from django.http import JsonResponse

def locationlist(request):
    locations = get_location()
    context = {
        'location_list': locations
    }
    return render(request, 'Location/locations.html', context)

def location_create(request):
    if request.method == 'POST':
        form = LocationForms(request.POST)
        if form.is_valid():
            create_location(form)
            messages.add_message(request, messages.SUCCESS, 'Location create successful')
            return HttpResponseRedirect(reverse('locationCreate'))
        else:
            print(form.errors)
    else:
        form = LocationForms()

    context = {
        'form': form,
    }

    return render(request, 'Location/locationCreate.html', context)

def location_by_product(request, product_name):
    locations = Location.objects.filter(producto__icontains=product_name)
    return render(request, "location_by_product.html", {"locations": locations})