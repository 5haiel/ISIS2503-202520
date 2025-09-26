import time
import json
import logging
from typing import Callable, Any, Optional

from django.conf import settings
from django.core.cache import cache
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)
DEFAULT_TTL = getattr(settings, "CACHE_DEFAULT_TTL", 60*5)

def make_key(*parts: str, version: Optional[int] = None) -> str:
    base = ":".join(str(p) for p in parts if p not in (None, ""))
    return f"{base}:v{version}" if version is not None else base

def _safe_serialize(obj: Any) -> str:
    try:
        return json.dumps(obj, default=lambda o: getattr(o, "__dict__", repr(o)))
    except Exception:
        return json.dumps({"__repr__": repr(obj)})

def _safe_deserialize(s: Optional[str]) -> Any:
    if s is None:
        return None
    try:
        return json.loads(s)
    except Exception:
        return s

def get_or_set(key: str,
               loader: Callable[[], Any],
               timeout: int = DEFAULT_TTL,
               version: Optional[int] = None,
               request=None) -> Any:
    """
    Cache-aside con lock. Si se pasa `request`, se setea request._cache_info con:
    { "hit": bool, "redis_ms": float, "db_ms": float, "total_ms": float }
    """
    k = make_key(key, version=version) if version else key
    start_total = time.time()
    # 1. intentar leer cache
    t0 = time.time()
    try:
        raw = cache.get(k)
    except Exception as e:
        logger.exception("Cache GET failed, fallback to loader: %s", e)
        raw = None
    t_redis_read = (time.time() - t0) * 1000  # ms

    if raw is not None:
        value = _safe_deserialize(raw)
        # registrar diagnósticos
        if request is not None:
            request._cache_info = {
                "hit": True,
                "redis_ms": t_redis_read,
                "db_ms": 0.0,
                "total_ms": (time.time() - start_total) * 1000,
            }
        return value

    # 2. MISS: intentar lock
    try:
        conn = get_redis_connection("default")
        lock = conn.lock(f"lock:{k}", timeout=10)
        have_lock = lock.acquire(blocking=False)
    except Exception:
        have_lock = False
        lock = None

    if have_lock:
        try:
            # re-check cache (otro proceso pudo haber llenado)
            t0 = time.time()
            raw = cache.get(k)
            t_redis_read2 = (time.time() - t0) * 1000
            if raw is not None:
                value = _safe_deserialize(raw)
                if request is not None:
                    request._cache_info = {
                        "hit": True,
                        "redis_ms": t_redis_read + t_redis_read2,
                        "db_ms": 0.0,
                        "total_ms": (time.time() - start_total) * 1000,
                    }
                return value

            # ejecutar loader (BD)
            tdb0 = time.time()
            value = loader()
            t_db = (time.time() - tdb0) * 1000

            # setear cache
            try:
                cache.set(k, _safe_serialize(value), timeout)
            except Exception:
                logger.exception("Cache SET failed")

            if request is not None:
                request._cache_info = {
                    "hit": False,
                    "redis_ms": t_redis_read + t_redis_read2,
                    "db_ms": t_db,
                    "total_ms": (time.time() - start_total) * 1000,
                }
            return value
        finally:
            try:
                lock.release()
            except Exception:
                pass
    else:
        # no obtuvimos lock: esperar y reintentar leer cache
        time.sleep(0.05)
        try:
            t0 = time.time()
            raw = cache.get(k)
            t_redis_read3 = (time.time() - t0) * 1000
            if raw is not None:
                value = _safe_deserialize(raw)
                if request is not None:
                    request._cache_info = {
                        "hit": True,
                        "redis_ms": t_redis_read + t_redis_read3,
                        "db_ms": 0.0,
                        "total_ms": (time.time() - start_total) * 1000,
                    }
                return value
        except Exception:
            pass
        # última opción: loader directo (evitar deadlock)
        tdb0 = time.time()
        value = loader()
        t_db = (time.time() - tdb0) * 1000
        if request is not None:
            request._cache_info = {
                "hit": False,
                "redis_ms": t_redis_read,
                "db_ms": t_db,
                "total_ms": (time.time() - start_total) * 1000,
            }
        return value

def invalidate(key: str, version: Optional[int] = None):
    k = make_key(key, version=version) if version else key
    try:
        cache.delete(k)
    except Exception:
        logger.exception("Error deleting cache key %s", k)
