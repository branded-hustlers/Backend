# Generated by Django 5.0.2 on 2024-05-15 04:23

import Customer.models
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0003_user_delete_staff_alter_customer_mobile_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CLERK', 'Clerk'), ('DELIVERY', 'Delivery'), ('ADMIN', 'Admin'), ('CUSTOMER', 'Customer')], default=Customer.models.Roles['CUSTOMER'], max_length=20),
        ),
    ]
