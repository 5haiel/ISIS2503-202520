from provesi.cache_utils import get_or_set, make_key
from ..repositories import get_order_with_product_and_location

CACHE_VERSION = 1
CACHE_TTL = 60 * 5  # 5 minutos, cambiar si conviene

def fetch_order_for_alistamiento(order_id: int, request=None) -> dict:
    key = make_key("order", order_id, version=CACHE_VERSION)
    # request se pasa para que get_or_set llene request._cache_info
    result = get_or_set(key, lambda: _load(order_id), timeout=CACHE_TTL, version=None, request=request)
    return result

def _load(order_id: int) -> dict:
    data = get_order_with_product_and_location(order_id)
    if data is None:
        # Decide: lanzar excepción o devolver {}
        return {}
    return data

def invalidate_order_cache(order_id: int):
    key = make_key("order", order_id, version=CACHE_VERSION)
    from provesi.cache_utils import invalidate
    invalidate(key)
