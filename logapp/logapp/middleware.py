# myapp/middleware.py

import logging
import time

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        # Get client IP address
        ip_address = self.get_client_ip(request)

        logger.info(
            f"{request.method} {request.path} {response.status_code} {duration:.2f}s - IP: {ip_address}"
        )

        return response
        
    def get_client_ip(self, request):
        """Get the client IP address from request"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            # Take the first IP if there are multiple
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip