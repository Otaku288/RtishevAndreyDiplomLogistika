# Generated by Django 5.1.7 on 2025-03-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото'),
        ),
        migrations.DeleteModel(
            name='Logistics',
        ),
    ]
