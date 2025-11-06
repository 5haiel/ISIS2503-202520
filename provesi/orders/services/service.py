from provesi.cache_utils import get_or_set, make_key
from ..repositories import get_order_with_product_and_location


def fetch_order_for_alistamiento(order_id: int, request=None) -> dict:
    return get_or_set(order_id, request=request)
