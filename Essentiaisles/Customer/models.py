from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if password is None:
            raise ValueError('Superusers must have a password')
        return self.create_user(email, password, **extra_fields)
    
class Customer(AbstractBaseUser):
    customer_id = models.IntegerField(primary_key=True)
    other_names = models.CharField(max_length=60)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    mobile_phone = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['other_names', 'last_name', 'mobile_phone', 'date_of_birth']

    objects = UserManager()

    class Meta:
        db_table = 'customer'
        managed = False
        

    def __str__ (self):
        return f"{self.last_name} {self.other_names}"
