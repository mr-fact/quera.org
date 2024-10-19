from django.http import JsonResponse, HttpResponseForbidden, HttpResponse

from django.core.cache import cache
from django.urls import resolve
from django.utils import timezone
from django.views.generic import DetailView
from rest_framework import status

from .models import BlockedIp, SecurityConfig, ViewDetail

from .utils import get_client_ip


class BlockIpMiddleware:
    maximum_rps = 4
    timeout = 60

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        view, _, _ = resolve(request.path)
        user_ip = get_client_ip(request)

        response = self.banned_before(user_ip)
        if response:
            return response

        LIMITED_VIEWS = SecurityConfig.objects.last().views.values_list(
            'path',
            flat=True)

        for url_path in LIMITED_VIEWS:
            response = self.validate_request_per_second(user_ip, url_path, timezone.now().timestamp())
            if response:
                return response

        response = self.get_response(request)

        return response

        pass

    def banned_before(self, user_ip):
        if BlockedIp.is_ip_blocked(user_ip):
            return HttpResponseForbidden()
        return None

    def validate_request_per_second(self, user_ip, url_path, current_time):
        requests = cache.get(f'ip_{user_ip}_{url_path}', [])
        last_second_requests = [request_time for request_time in requests if request_time > (current_time - 1)]
        if len(last_second_requests) > 4:
            BlockedIp.objects.create(
                ip = user_ip,
                view=DetailView.objects.get(path=url_path)
            )
            return HttpResponse(status=429)
        return None

