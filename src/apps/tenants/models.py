from django.db import models

# Create your models here.
from apps.module.models import Module

class Tenants(models.Model):
    
    
    class Industry(models.TextChoices):
        IT = 'it', 'IT'
        FINANCE = 'finance', 'FINANCE'
        AGRO = 'agro', 'AGRO'
        RETAIL = 'retail', 'RETAIL'
        LOGISTICS = 'logistics', 'LOGISTICS'
        MANUFACTURING = 'manufacturing', 'MANUFACTURING'
        HEALTH = 'health', 'HEALTH'
        EDUCATION = 'education', 'EDUCATION'
        MEDIA = 'media', 'MEDIA'
        OTHER = 'other', 'OTHER'
    
    name = models.CharField(max_length=50)
    company_slug = models.CharField(max_length=10)
    
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    
    full_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=20, choices=Industry.choices, default=Industry.OTHER)
    
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.name}"
    
    
    class Meta:
        db_table = 'tenants'
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
    
    
    
class TenantModules(models.Model):
    
    
    class Plan(models.TextChoices):
        STANDART = 'standart', 'STANDART'
        PRO = 'pro', 'PRO'
        PREMIUM = 'premium', 'PREMIUM'
    
    tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    plan = models.CharField(max_length=10, choices=Plan.choices, default=Plan.STANDART)
    
    def __str__(self):
        return f"{self.tenant.name} - {self.module.name}"
    
    
    class Meta:
        db_table = 'tenant_modules'
        verbose_name = 'Tenant Module'
        verbose_name_plural = 'Tenant Modules'
    
    
