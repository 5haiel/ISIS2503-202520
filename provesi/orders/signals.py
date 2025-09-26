from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from .models import Orders
from .services import invalidate_order_cache

@receiver(post_save, sender=Orders)
def on_order_change(sender, instance, created, **kwargs):
    # invalidar después del commit para garantizar consistencia
    transaction.on_commit(lambda: invalidate_order_cache(instance.id))

@receiver(post_delete, sender=Orders)
def on_order_delete(sender, instance, **kwargs):
    transaction.on_commit(lambda: invalidate_order_cache(instance.id))
