from django.contrib import admin

# Register your models here.
from .models import DeviceLog

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'timestamp')
    list_filter = ('ip_address',)
    
    class Meta:
        verbose_name = 'Device Log'
        verbose_name_plural = 'Device Logs'