from .models import DeviceLog

class DeviceLogService:
    
    
    @classmethod
    def create_device_log(
        cls,
        ip_address: str,
        browser: str | None = None,
        os: str | None = None,
        device_name: str | None = None,
    ):
        
        exists = DeviceLog.objects.filter(ip_address=ip_address).exists()
        
        if not exists:
            DeviceLog.objects.create(
                ip_address=ip_address,
                browser=browser,
                os=os,
                device_name=device_name,
            )
        else:
            device_log = DeviceLog.objects.get(ip_address=ip_address)
            device_log.count += 1
            device_log.save()
            
