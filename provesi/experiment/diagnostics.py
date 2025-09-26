import time

class CacheDiagnosticsMiddleware:
    """
    Middleware estilo 'new' (callable). Mide tiempos y carga
    información en request._cache_info para que la vista / cache layer
    la use y el response pueda exponer cabeceras.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request._req_start_time = time.time()
        response = self.get_response(request)
        total_ms = int((time.time() - getattr(request, "_req_start_time", time.time())) * 1000)
        cache_info = getattr(request, "_cache_info", {})
        response.setdefault("X-Total-Time-ms", str(total_ms))
        response.setdefault("X-Cache-Hit", str(cache_info.get("hit", False)))
        if "redis_ms" in cache_info:
            response.setdefault("X-Redis-Time-ms", str(int(cache_info["redis_ms"])))
        if "db_ms" in cache_info:
            response.setdefault("X-DB-Time-ms", str(int(cache_info["db_ms"])))
        return response
