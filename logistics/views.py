from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Order
from .forms import OrderForm, Price

def product_list(request):
    query = request.GET.get('q', '').capitalize()
    products = Product.objects.all()
    form = Price(request.GET or None)
    if form.is_valid():
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        product_type = form.cleaned_data.get('product_type')
        color = form.cleaned_data.get('color')
        if product_type:
            products = products.filter(type = product_type)
        if color:
            if color != 'Все цвета':
                products = products.filter(color = color)
        if min_price:
            products = products.filter(price__gte = min_price)
        if max_price:
            products = products.filter(price__lte = max_price)
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    return render(request, 'logistics/product_list.html', {'products': products, 'query': query, 'form': form})

@login_required
def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.company = request.user
            order.product = product
            order.save()
            return redirect('order_success', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'logistics/order_create.html', {'form': form, 'product': product})

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, company=request.user)
    return render(request, 'logistics/order_success.html', {'order': order})

@login_required
def company_orders(request):
    orders = Order.objects.filter(company=request.user)
    return render(request, 'logistics/company_orders.html', {'orders': orders})

def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    
    order.delete()
    return redirect('company_orders')

@login_required
def warranty(request):
    return render(request, 'logistics/warranty.html')


@login_required
def contact(request):
    return render(request, 'logistics/contact.html')

@login_required
def delivery(request):
    return render(request, 'logistics/delivery.html')

