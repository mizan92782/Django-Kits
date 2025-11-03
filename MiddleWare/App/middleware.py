from ipaddress import ip_address
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from datetime import datetime
class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Before view: Request is coming...")
        ip= request.META.get('REMOTE_ADDR')
        path = request.META.get('PATH_INFO')
        print(ip)
        print(path)

        
    
    def process_response(self, request, response):
        
        print("After view: Response is going...")
        
        
        return response
