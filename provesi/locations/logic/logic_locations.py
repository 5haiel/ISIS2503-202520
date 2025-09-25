from ..models import Location

def get_location():
    queryset = Location.objects.all().order_by('producto')[:10]
    return (queryset)

def create_location(form):
    location = form.save()
    location.save()
    return ()

def get_locations_by_product(product_name):
    return Location.objects.filter(producto__icontains=product_name)