from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import OrderForm


def _get_client_ip(request: HttpRequest) -> str:
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    return forwarded.split(',')[0].strip() if forwarded else request.META.get('REMOTE_ADDR', '')


def _get_device_type(user_agent: str) -> str:
    ua = user_agent.lower()
    if any(k in ua for k in ('iphone', 'android', 'mobile')):
        return 'mobile'
    if any(k in ua for k in ('ipad', 'tablet')):
        return 'tablet'
    return 'desktop'


def create_order(request: HttpRequest):
    form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.ip_address = _get_client_ip(request)
            order.user_agent = request.META.get('HTTP_USER_AGENT', '')
            order.device_type = _get_device_type(order.user_agent)
            order.save()
            return redirect('apps.landing:landing_page')

    return render(request, 'order.html', {'form': form})