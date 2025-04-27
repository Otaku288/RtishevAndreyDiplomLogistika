from django.contrib import admin
from .models import Product, Order, ProductType

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'weight')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'product', 'quantity', 'status')

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


