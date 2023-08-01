from functools import wraps

from django.core.cache import cache


def cache_queryset_by_user(view_func):
    @wraps(view_func)
    def _wrapped_view(self, request, *args, **kwargs):
        cache_key = request.user.id
        cached_queryset = cache.get(cache_key)

        if cached_queryset is None:
            queryset = view_func(self, request, *args, **kwargs)
            cache.set(cache_key, queryset)
        else:
            queryset = cached_queryset

        return queryset

    return _wrapped_view
