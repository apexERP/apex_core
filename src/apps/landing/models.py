from django.db import models

# Create your models here.



class DeviceLog(models.Model):
    
    ip_address = models.GenericIPAddressField()
    browser = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=100, blank=True, null=True)
    device_name = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.ip_address
    
    
    
    class Meta:
        verbose_name = 'Device Log'
        verbose_name_plural = 'Device Logs'
        db_table = 'device_logs'


