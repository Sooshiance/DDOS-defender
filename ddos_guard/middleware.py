from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


MAX_LIMIT_REQUEST = settings.MAX_LIMIT_REQUEST


class RequestLimitMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Get the request count from the cache or initialize it to zero
        request_count = cache.get('request_count', 0)
        # Check if the request limit is reached
        if request_count >= MAX_LIMIT_REQUEST:
            # Return a custom response or raise an exception
            # or
            # raise Exception('Request limit exceeded')
            return HttpResponse('Request limit exceeded', status=429)

        # Increment the request count and save it to the cache
        request_count += 1
        cache.set('request_count', request_count)

        # Pass the request to the next middleware or view
        response = self.get_response(request)

        return response
