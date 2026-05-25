from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.



def landing_page(request: HttpRequest):
    return render(request, 'landing.html')