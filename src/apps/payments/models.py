from django.db import models
from apps.tenants.models import Tenants
from core.softdelete import SoftDeleteModel


class TenantPayments(SoftDeleteModel):
    
    tenant = models.ForeignKey(Tenants, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    from_date = models.DateField()
    to_date = models.DateField()
        
    class Meta:
        db_table = 'tenant_payments'
        verbose_name = 'Tenant Payment'
        verbose_name_plural = 'Tenant Payments'
    
    
    def __str__(self):
        return f"{self.tenant.name} {self.amount}" 
    

    def __repr__(self):
        return f"{self.tenant.name} {self.amount}"
    
    
