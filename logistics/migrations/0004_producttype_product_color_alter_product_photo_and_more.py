# Generated by Django 5.1.7 on 2025-04-15 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0003_alter_product_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название типа')),
                ('description', models.CharField(max_length=255, verbose_name='Описание типа')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Белый', max_length=100, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default='products/Без_названия.jpg', null=True, upload_to='products/', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='logistics.producttype', verbose_name='Тип'),
        ),
    ]
