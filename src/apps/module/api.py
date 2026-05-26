from django.http import JsonResponse, HttpRequest

from .models import Module, ModulePrice
from .serializers import ModuleSerializer, ModulePriceSerializer, ModuleDetailSerializer


def get_all_modules(request: HttpRequest):

    modules = Module.objects.all()

    serializer = ModuleSerializer(modules, many=True)

    return JsonResponse(serializer.data, safe=False)



def get_module(request: HttpRequest, id: int):

    module = (
        Module.objects.
        prefetch_related('prices')
        .get(id=id)
    )

    serializer = ModuleDetailSerializer(module)

    return JsonResponse(serializer.data, safe=False)


def get_all_module_prices(request: HttpRequest):

    module_prices = ModulePrice.objects.all()

    serializer = ModulePriceSerializer(module_prices, many=True)

    return JsonResponse(serializer.data, safe=False)


