from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(AbstractUser):
    company_name = models.CharField(max_length=100, verbose_name="Название компании")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон")
    warehouse_address = models.TextField(verbose_name="Адрес склада")

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"