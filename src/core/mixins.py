from django.core.cache import cache

from config.settings.const import MINUTE


class CachePagePerUserMixin:
    cache_timeout = MINUTE

    def get_cache_key(self, request, *args, **kwargs):
        user_id = self.get_user_id_from_request(request)
        if user_id is None:
            return None

        view_name = self.__class__.__name__
        cache_key = f"{view_name}:{user_id}"
        return cache_key

    def get_user_id_from_request(self, request):
        if request.user.is_authenticated:
            return request.user.id
        return None

    def dispatch(self, request, *args, **kwargs):
        cache_key = self.get_cache_key(request, *args, **kwargs)
        if cache_key is None:
            return super().dispatch(request, *args, **kwargs)

        response = cache.get(cache_key)

        if not response:
            response = super().dispatch(request, *args, **kwargs)
            response.render()
            cache.set(cache_key, response, self.cache_timeout)

        return response
