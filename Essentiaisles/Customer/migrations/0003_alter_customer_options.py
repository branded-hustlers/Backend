# Generated by Django 5.0.2 on 2024-04-15 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0002_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'managed': False},
        ),
    ]
