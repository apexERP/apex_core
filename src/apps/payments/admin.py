from django.contrib import admin

from .models import TenantPayments


@admin.register(TenantPayments)
class TenantPaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'from_date', 'to_date')
    list_filter = ('tenant', 'from_date', 'to_date')
    
    
