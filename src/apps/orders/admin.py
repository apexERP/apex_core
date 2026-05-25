from django.contrib import admin

# Register your models here.
from .models import Orders



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone_number', 'order_status')
    list_filter = ('order_status',)