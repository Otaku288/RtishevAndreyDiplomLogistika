from django.db import models
from accounts.models import Company

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    dimensions = models.CharField(max_length=50, verbose_name="Габариты")
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вес")
    photo = models.ImageField(upload_to='products/', verbose_name="Фото", null=True, blank=True, default='products/Без_названия.jpg')
    color = models.CharField(max_length=100, verbose_name="Цвет", default='Белый')
    type = models.ForeignKey('ProductType', on_delete=models.CASCADE, verbose_name='Тип', null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Order(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="Компания")
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    warehouse_address = models.TextField(verbose_name="Адрес склада")
    delivery_date = models.DateField(verbose_name="Дата доставки")
    status = models.CharField(max_length=50, default='Pending', verbose_name="Статус")

    def __str__(self):
        return f"Заказ #{self.id} - {self.company.company_name}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"



class ProductType(models.Model):
    name  = models.CharField(max_length=150, verbose_name="Название типа")
    description = models.CharField(max_length=255, verbose_name="Описание типа")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"