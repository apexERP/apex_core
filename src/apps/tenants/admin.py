from django.contrib import admin

# Register your models here.
from .models import TenantModules, Tenants
from apps.module.models import Module, ModulePrice



# class TenantModulesInline(admin.TabularInline):
#     model = TenantModules
#     extra = 2


class TenantModulesInline(admin.TabularInline):
    model = TenantModules
    extra = 2
    
    # Add your custom method to the fields layout
    fields = ['module', 'plan', 'get_calculated_price']
    
    # Read-only fields must be declared explicitly in Django inlines
    readonly_fields = ['get_calculated_price']

    def get_calculated_price(self, instance):
        """Fetches the corresponding price based on the selected module and tier plan."""
        if not instance or not instance.pk or not instance.module:
            return "$0 (Save to calculate)"

        # Fetch the price record for the selected module
        price_record = ModulePrice.objects.filter(module=instance.module).first()
        if not price_record:
            return "Price mapping not set"

        # Dynamically fetch the matching price field based on the plan string
        # e.g., if plan is 'pro', matches 'pro_price'
        plan_str = instance.plan.lower()  # ensures it matches 'standart', 'pro', or 'premium'
        price_attr = f"{plan_str}_price"
        
        try:
            price = getattr(price_record, price_attr, 0)
            return f"${price:,}"
        except AttributeError:
            return "$0"

    # Give the column a nice descriptive header in the admin UI
    get_calculated_price.short_description = "Active Price"

@admin.register(Tenants)
class TenantsAdmin(admin.ModelAdmin):
    inlines = [TenantModulesInline]
    
    list_display = ['name', 'company_slug', 'phone_number', 'full_name']
    
    


