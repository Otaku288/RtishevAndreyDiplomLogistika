from django import forms
from .models import Order, ProductType, Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'warehouse_address', 'delivery_date']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'type': 'date'}),
        }

class Price(forms.Form):
    CHOICES = (
        ('Все цвета', 'Все цвета'),
        ('Белый', 'Белый'), 
        ('Коричневый', 'Коричневый'),
    )
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    product_type = forms.ModelChoiceField(required=False, queryset=ProductType.objects.all(), empty_label='Вся мебель')
    color = forms.ChoiceField(choices = CHOICES, required=False)

