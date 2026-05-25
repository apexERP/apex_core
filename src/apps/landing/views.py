from django.shortcuts import render
from django.http import HttpRequest

from user_agents import parse  

from .models import DeviceLog
from .utils import get_client_ip
from .service import DeviceLogService


def landing_page(request: HttpRequest):
    
    ip = get_client_ip(request)
    
    ua = parse(request.META.get('HTTP_USER_AGENT', ''))
    
    DeviceLogService.create_device_log(
        ip_address=ip,
        browser=ua.browser.family,
        os=ua.os.family,
        device_name=ua.device.family,
    )
    
    return render(request, 'landing.html')


