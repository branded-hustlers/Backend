# Generated by Django 5.0.2 on 2024-05-15 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_stock', models.PositiveIntegerField()),
                ('minimum_stock', models.PositiveIntegerField()),
                ('maximum_stock', models.PositiveIntegerField()),
                ('reorder_quantity', models.PositiveIntegerField()),
                ('storage_location', models.CharField(max_length=30)),
                ('shelf_life', models.DateTimeField()),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
    ]