

from django.urls import path

from .api import get_all_modules, get_all_module_prices, get_module


app_name = 'apps.module'

urlpatterns = [
    path("", get_all_modules),
    path("<int:id>/", get_module),
    path("prices/", get_all_module_prices),
]


