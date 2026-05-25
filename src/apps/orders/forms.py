
from django.forms import ModelForm, TextInput


from .models import Orders


class OrderForm(ModelForm):
    
    class Meta:
        model = Orders
        fields = ['first_name', 'phone_number']
        labels = {
            'first_name': 'First Name',
            'phone_number': 'Phone Number',
        }
        
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'phone_number': TextInput(attrs={'class': 'form-control'}),
        }
        
