from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('order/<int:product_id>/', views.order_create, name='order_create'),
    path('order/success/<int:order_id>/', views.order_success, name='order_success'),
    path('my-orders/', views.company_orders, name='company_orders'),
    path('warranty/', views.warranty, name='warranty'),
    path('contact/', views.contact, name='contact'),
    path('delivery/', views.delivery, name='delivery'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),
]