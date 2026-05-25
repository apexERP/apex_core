from django.contrib import admin

# Register your models here.
from .models import Module, ModulePrice




class ModulePriceInline(admin.TabularInline):
    model = ModulePrice
    extra = 1
    

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    
    inlines = [ModulePriceInline]   
    
    list_display = ('name', 'title', 'description', 'image', 'order')
    ordering = ['order']
    
    
