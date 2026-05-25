from django.http.request import HttpRequest
from user_agents import parse


def get_client_ip(request: HttpRequest):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    
    return ip




def device_info(request: HttpRequest):
    
    user_agent_string = request.META.get('HTTP_USER_AGENT', '')
    
    user_agent = parse(user_agent_string)
    
    return {
        "browser": user_agent.browser.family,
        "os": user_agent.os.family,
        "device": user_agent.device.family,
        "is_mobile": user_agent.is_mobile,
        "is_tablet": user_agent.is_tablet,
        "is_pc": user_agent.is_pc,
        "is_tablet": user_agent.is_tablet
    }
    
#     {
#     'browser': 'Firefox',
#     'os': 'Windows',
#     'device': 'Other',
#     'is_mobile': False,
#     'is_pc': True,
#      }