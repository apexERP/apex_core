from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import OrderForm
# Create your views here.



def create_order(request: HttpRequest):
    
    form = OrderForm()
    
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('apps.landing:landing_page')
            
                
    return render(request, 'order.html', {'form': form})


