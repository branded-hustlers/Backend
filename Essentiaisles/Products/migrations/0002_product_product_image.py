# Generated by Django 5.0.2 on 2024-04-15 20:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='product_images'),
            preserve_default=False,
        ),
    ]