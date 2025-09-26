from django.shortcuts import render
from .forms import InventoryForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_inventory import create_inventory, get_inventory

def inventory_list(request):
    inventarios = get_inventory()
    context = {
        'inventory_list': inventarios
    }
    return render(request, 'Inventory/inventarios.html', context)

def inventory_create(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            create_inventory(form)
            messages.add_message(request, messages.SUCCESS, 'inventory create successful')
            return HttpResponseRedirect(reverse('inventoryCreate'))
        else:
            print(form.errors)
    else:
        form = InventoryForm()

    context = {
        'form': form,
    }

    return render(request, 'inventory/inventoryCreate.html', context)
