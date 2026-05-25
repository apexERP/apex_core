from django.contrib import admin

# Register your models here.
from .models import Users

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "role",
        "is_active",
        "is_staff",
    )
    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )
    
    ordering = ["email"]