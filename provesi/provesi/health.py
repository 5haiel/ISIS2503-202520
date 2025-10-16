from django.http import JsonResponse
from django.core.cache import cache
from django.db import connection

def healthz(request):
    ok_db = ok_cache = True
    try:
        with connection.cursor() as c: c.execute("SELECT 1")
    except Exception:
        ok_db = False
    try:
        cache.get("ping")
    except Exception:
        ok_cache = False
    status = 200 if (ok_db and ok_cache) else 503
    return JsonResponse({"db": ok_db, "cache": ok_cache}, status=status)
